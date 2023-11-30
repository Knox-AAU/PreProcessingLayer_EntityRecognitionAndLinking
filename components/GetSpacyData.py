import json, os
import sys
from langdetect import detect
from typing import List
from lib.EntityLinked import EntityLinked

from lib.Exceptions.UndetectedLanguageException import (
    UndetectedLanguageException,
)
from lib.JSONEntityOutput import JSONEntityOutput

sys.path.append(".")
from lib.Entity import Entity
import en_core_web_lg
import da_core_news_lg

nlp_en = en_core_web_lg.load()
nlp_da = da_core_news_lg.load()


# GetText shall get text from pipeline del A
def GetText(title: str):
    file = open(title, "r")

    stringWithText = file.read()

    file.close
    return stringWithText


def GetTokens(text: str):
    result = DetectLang(text)
    if result == "da":
        return nlp_da(text)
    elif result == "en":
        return nlp_en(text)
    else:
        raise UndetectedLanguageException()


def DetectLang(text: str):
    stringdata = str(text)
    language = detect(stringdata)
    return language


# Method to fully extract entity mentions, find the sentences and calculate indexes and finally create a final JSON
def BuildJSONFromEntities(entities: List[EntityLinked], doc, fileName: str) -> JSONEntityOutput:
    if not os.path.exists("entity_mentions.json"):
        open("entity_mentions.json", "w").close()

    # Create a list of sentences with their entities in the desired JSON format
    currentJson = open("./entity_mentions.json", "r")
    currentJson.seek(0, os.SEEK_END)
    if currentJson.tell():
        currentJson.seek(0)
        currentJson = json.load(currentJson)
    else:
        currentJson = []

    sentences_json = []

    for entity in entities:
        # Use the 'start' and 'end' indexes of the entity to get its index within its sentence
        sentence = entity.sentence

        entityJSON = entity.getEntityJSON()

        found = False
        for sentence_info in sentences_json:
            if sentence_info["sentence"] == sentence.replace("\n", ""):
                sentence_info["entityMentions"].append(entityJSON)
                found = True
                break

        if not found:
            sentences_json.append(
                {
                    "sentence": sentence.replace("\n", ""),
                    "sentenceStartIndex": entity.sentenceStartIndex,
                    "sentenceEndIndex": entity.sentenceEndIndex,
                    "entityMentions": [entityJSON],
                }
            )

    # Create the final JSON structure
    final_json = {
        "fileName": fileName,
        "language": DetectLang(doc),
        "metadataId":"7467628c-ad77-4bd7-9810-5f3930796fb5",
        "sentences": sentences_json,
    }
    if len(currentJson) != 0:
        for index in currentJson:
            if index["fileName"] == final_json["fileName"]:
                return JSONEntityOutput(final_json, currentJson)
            else:
                currentJson.append(final_json)
    else:
        currentJson.append(final_json)
    return JSONEntityOutput(final_json, currentJson)

def GetEntities(doc) -> List[Entity]:
    entities = []
    for entity in doc.ents:
        entities.append(
            Entity(
                name=entity.text,
                startIndex=entity.start_char,
                endIndex=entity.end_char,
                sentence=entity.sent.text,
                sentenceStartIndex=entity.sent.start_char,
                sentenceEndIndex=entity.sent.end_char,
                label=entity.label_,
                type=isLiteral(entity),
            )
        )

    return entities

def isLiteral(entity):
    if entity.label_ == "DATE" or entity.label_ == "TIME" or entity.label_ == "PERCENT" or entity.label_ == "MONEY" or entity.label_ == "QUANTITY" or entity.label_ == "ORDINAL" or entity.label_ == "CARDINAL":
        return "Literal"
    else:
        return "Entity"