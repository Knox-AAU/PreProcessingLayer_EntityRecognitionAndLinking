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
    

@app.get('/{articlename}/entities')
async def getentities(articlename: str):
    await main()
    with open('entity_mentions.json', 'r') as entityJson:
        entityMentions = json.load(entityJson)
    entitiesfromarticle = []
    for elem in entityMentions:
        path = elem["fileName"]
        name = path.split('/');
        if(name[-1] == articlename):
            entitiesfromarticle.append(elem)
 

    return(entitiesfromarticle)
    
   
    

async def main():
    #FileWatcher(filename = "Artikel.txt", interval = 5.0, callback=lambda :print("whatever")).start() #Starts fileWatcher
    
    text = GetSpacyData.GetText("Artikel.txt") #Takes in title of article. Gets article text in string format
    doc = GetSpacyData.GetTokens(text) #finds entities in text, returns entities in doc object
    ents = GetSpacyData.GetEntities(doc, "Artikel.txt") #appends entities in list
    entMentions= GetSpacyData.entityMentionJson(ents)  #Returns JSON object containing an array of entity mentions

    await Db.InitializeIndexDB('./Database/DB.db') #makes the DB containing the entities of KG
    # just to try out the CRUD below
    await Db.Insert('./Database/DB.db',"EntityIndex", "Martin Kjærs") #Inserts entity into "INDEX" table
    await Db.Insert('./Database/DB.db',"EntityIndex", "Alija")
    await Db.Insert('./Database/DB.db',"EntityIndex", "Bossmundur")
    #Db.Update('./Database/DB.db',"EntityIndex", 2, "Alija Cerimagic")
    #Db.Delete('./Database/DB.db',"EntityIndex", 1)
    await Db.SortDB('./Database/DB.db', "EntityIndex") #Sorting DB
    entsFromDB = await Db.Read('./Database/DB.db',"EntityIndex") #Read returns array of tuples of each row of the table
    
    print("ENTS FROM DB")
    print(entsFromDB)

    entLinks = await entitylinkerFunc(ents) #Returns JSON object containing an array of entity links

    with open('entity_mentions.json', 'w') as entityJson:
        json.dump(entMentions, entityJson)
