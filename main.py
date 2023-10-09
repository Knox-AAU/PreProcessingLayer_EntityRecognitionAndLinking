from components import *
import sys
import json

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startEvent():
    main()

@app.get('/entitymentions')
def getJson():
    with open('entity_mentions.json', 'r') as entityJson:
        return(json.load(entityJson))
    

def main():
    doc = GetSpacyData.GetTokens("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")
    ents = GetSpacyData.GetEntities(doc)
    print(ents)
if __name__ == '__main__':
    sys.exit(main())
