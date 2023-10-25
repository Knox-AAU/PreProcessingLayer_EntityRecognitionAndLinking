import spacy, json
import sys

sys.path.append(".")
from lib.Entity import Entity

nlp = spacy.load("da_core_news_cstm")

# GetText skal få text fra pipeline del A
def GetText(title):
    file = open(title, "r")

    stringWithText = file.read()

    file.close
    return stringWithText

def GetTokens(text):
    doc = nlp(text)
    print(type(doc))
    return doc

#Method to fully extract entity mentions, find the sentences and calculate indexes and finally create a final JSON
def GetEntities(doc, fileName):
    # Create a dictionary of sentences
    sentence_entities = {}

    for entity in doc.ents:
        # Use the 'start' and 'end' indexes of the entity to get its index within its sentence
        entity_start_char = entity.start_char - entity.sent.start_char
        entity_end_char = entity.end_char - entity.sent.start_char

        sentence = entity.sent.text
        name = entity.text
        start_index = entity_start_char
        end_index = entity_end_char

        entity = Entity(name, start_index, end_index, fileName)

        if sentence in sentence_entities:
            sentence_entities[sentence].append(entity)
        else:
            sentence_entities[sentence] = [entity]

    # Create a list of sentences with their entities in the desired JSON format
    sentences_json = []
    for sentence, entities in sentence_entities.items():
        entity_mentions = []
        for entity in entities:
            entity_mentions.append({
                "name": entity.name,
                "startIndex": entity.startIndex,
                "endIndex": entity.endIndex
            })
        sentences_json.append({
            "sentence": sentence,
            "entityMentions": entity_mentions
        })
    
    # Create the final JSON structure
    final_json = {
        "fileName": fileName,
        "sentences": sentences_json
    }

    return final_json

def entityMentionJson(ents):
    entityMentions = []
    for ent in ents:
        entityMentions.append(ent.getEntity())
    return entityMentions