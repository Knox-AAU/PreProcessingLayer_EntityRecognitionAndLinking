from components import *
from components.EntityLinker import entitylinkerFunc
import sys, json
from lib.FileWatcher import FileWatcher

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startEvent():
    await main()

@app.get('/entitymentions')
async def getJson():
    await main()
    with open('entity_mentions.json', 'r') as entityJson:
        entityMentions = json.load(entityJson)
        return(entityMentions)
    

async def main():
    FileWatcher(filename = "Artikel.txt", interval = 5.0, callback=lambda :print("whatever")).start() #Starts fileWatcher
    
    text = GetSpacyData.GetText("Artikel.txt") #Takes in title of article. Gets article text in string format
    doc = GetSpacyData.GetTokens(text) #finds entities in text, returns entities in doc object
    ents = GetSpacyData.GetEntities(doc, "Artikel.txt") #appends entities in list
    entMentions= GetSpacyData.entityMentionJson(ents)  #Returns JSON object containing an array of entity mentions

    await Db.InitializeIndexDB()#makes the DB containing the entities of KG
    # just to try out the CRUD below
    Db.Insert("EntityIndex", "Martin Kjærs") #Inserts entity into "INDEX" table
    Db.Update("EntityIndex", 2, "Alija Cerimagic")
    Db.Delete("EntityIndex", 1)
    entsFromDB = Db.Read("EntityIndex") #Read returns array of tuples of each row of the table
    
    print(entsFromDB)

    entLinks = entitylinkerFunc(entMentions) #Returns JSON object containing an array of entity links

    print(entMentions)

    with open('entity_mentions.json', 'w') as entityJson:
        json.dump(entMentions, entityJson)

if __name__ == '__main__':
    sys.exit(main())
