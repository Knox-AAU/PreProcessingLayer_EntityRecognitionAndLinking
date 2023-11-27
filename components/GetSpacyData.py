import json, os
import sys
from langdetect import detect
from typing import List
from lib.EntityLinked import EntityLinked

from lib.Exceptions.UndetectedLanguageException import (
    UndetectedLanguageException,
)

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