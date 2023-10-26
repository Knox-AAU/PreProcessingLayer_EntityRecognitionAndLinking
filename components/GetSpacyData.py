import spacy, json
import sys

sys.path.append(".")
from lib.Entity import Entity


nlp = spacy.load("en_core_web_md")


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


def GetEntities(doc, fileName):
    ents = []
    for entity in doc.ents:
        ent = Entity(entity.text, entity.start_char, entity.end_char, fileName)
        ents.append(ent)
    return ents


def entityMentionJson(ents):
    entityMentions = []
    for ent in ents:
        entityMentions.append(ent.getEntity())
    return entityMentions
