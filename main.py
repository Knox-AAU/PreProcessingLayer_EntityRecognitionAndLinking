from components import *
import sys
import json

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
    doc = GetSpacyData.GetTokens("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")
    ents = GetSpacyData.GetEntities(doc) 
    with open('entity_mentions.json', 'w') as entityJson:
        json.dump(ents, entityJson)

if __name__ == '__main__':
    sys.exit(main())
