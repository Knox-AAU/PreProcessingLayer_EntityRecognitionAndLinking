import spacy
from lib.ent import Entity
nlp = spacy.load("da_core_news_cstm")



def GetTokens(string):
    doc = nlp(string)
    return doc
    
def GetEntities(doc):
    ents = []
    for entity in doc.ents: 
        ent = Entity(entity.text, (entity.start_char, entity.end_char))
        ents.append(ent)
    return ents


