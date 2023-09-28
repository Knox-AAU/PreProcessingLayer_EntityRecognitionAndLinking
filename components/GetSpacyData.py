import spacy

nlp = spacy.load("da_core_news_cstm")



def getspacydataFunc(string):
    doc = nlp(string)
    return doc
    
    