
import os
from typing import List
from components import Db
from components import GetSpacyData
from components.GetSpacyData import DetectLang
from lib.EntityLinked import EntityLinked


async def insertEntitiesInDb(dbPath: str, fileName: str, entityLinks: List[EntityLinked]):
    sentences_dict = {}
    
    for entity in entityLinks:
        sentenceId = None
        if entity.sentence not in sentences_dict:
            sentenceId = await Db.Insert(
                dbPath, 
                "sentence", 
                {
                    "text": entity.sentence, 
                    "fileName": fileName, 
                    "startIndex": entity.sentenceStartIndex, 
                    "endIndex": entity.sentenceEndIndex
                }
            )
            sentences_dict[entity.sentence] = sentenceId
        else:
            sentenceId = sentences_dict[entity.sentence]

        setattr(entity, "sid", sentenceId)
        setattr(entity, "fileName", fileName)
        await Db.Insert(dbPath, "entitymention", entity)   

         

async def fetchAllEntityMentions(dbPath: str, dirPath: str):
    final_json = []
    for f in os.listdir(dirPath):
        fullPath = dirPath + f
        text = GetSpacyData.GetText(fullPath) 
        final_json.append(await fetchEntityMentions(dbPath, fullPath, text))
    return final_json

async def fetchEntityMentions(dbPath: str, fileName: str, fullText):
    entitiesWithSentences = await Db.JoinOnFileName(
        dbPath, 
        [
            "entitymention.name",
            "entitymention.startIndex", 
            "entitymention.endIndex", 
            "entitymention.label", 
            "entitymention.type", 
            "entitymention.iri",
            "sentence.text",
            "sentence.startIndex",
            "sentence.endIndex",
        ],
        "entitymention",
        "sentence",
        "sid",
        fileName
    )
    if len(entitiesWithSentences) == 0:
        return []

    json = []
    sentences_json = []

    for entity in entitiesWithSentences:
        entityJSON = {
            "name": entity[0],
            "startIndex": entity[1],
            "endIndex": entity[2],
            "label": entity[3],
            "type": entity[4],
            "iri": ("knox-kb01.srv.aau.dk/" + entity[5]) if entity[4] == "Entity" else None
        }
            
        found = False
        for sentence in sentences_json:
            if sentence["sentence"] == entity[6]:
                sentence["entityMentions"].append(entityJSON)
                found = True
                break

        if not found:
            sentences_json.append(
                {
                    "sentence": entity[6],
                    "sentenceStartIndex": entity[7],
                    "sentenceEndIndex": entity[8],
                    "entityMentions": [entityJSON],
                }
            )
        
    json.append(
        {
            "fileName": fileName,
            "language": DetectLang(fullText),
            "sentences": sentences_json,
        }
    )

    return json
