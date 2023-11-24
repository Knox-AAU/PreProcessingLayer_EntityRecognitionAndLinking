import string
from components import *
from components.EntityLinker import entitylinkerFunc
from components.EntityLinker import GetAllEntities
import sys, json, os
from multiprocessing import Process
from lib.Exceptions.ArticleNotFoundException import ArticleNotFoundException
from lib.Exceptions.InputException import InputException
from lib.Exceptions.UndetectedLanguageException import (
    UndetectedLanguageException,
)
from lib.DirectoryWatcher import DirectoryWatcher
from langdetect import detect
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="public")
app = FastAPI(title="API")

dirWatcher = DirectoryWatcher(directory = "data_from_A", callback=lambda file_path :print("whatever" + file_path))


@app.on_event("startup")
async def startEvent():
    dirWatcher.start_watching() #Starts DirectoryWatcher

@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down...")
    dirWatcher.stop_watching()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

    


@app.get("/entitymentions")
async def getJson():
    await main()
    with open("entity_mentions.json", "r") as entityJson:
        entityMentions = json.load(entityJson)
        return entityMentions


@app.get("/{articlename}/entities")
async def getentities(articlename: str):
    await main()
    with open("entity_mentions.json", "r") as entityJson:
        entityMentions = json.load(entityJson)
    for elem in entityMentions:
        path = elem["fileName"]
        name = path.split("/")
        if name[-1] == articlename:
            return elem
    raise HTTPException(status_code=404, detail="Article not found")


@app.post("/detectlanguage")
async def checklang(request: Request):
    data = await request.body()
    stringdata = str(data)
    print(len(stringdata))
    if len(stringdata) < 4:
        raise HTTPException(status_code=400, detail="Text is too short")

    language = detect(stringdata)

    return language


async def main():
    if not os.path.exists("entity_mentions.json"):
        open("entity_mentions.json", "w").close()

    text = GetSpacyData.GetText(
        "Artikel.txt"
    )  # Takes in title of article. Gets article text in string format
    doc = GetSpacyData.GetTokens(
        text
    )  # finds entities in text, returns entities in doc object

    text = GetSpacyData.GetText(
        "Artikel.txt"
    )  # Takes in title of article. Gets article text in string format

    try:
        doc = GetSpacyData.GetTokens(
            text
        )  # finds entities in text, returns entities in doc object
    except UndetectedLanguageException:
        raise HTTPException(status_code=400, detail="Undetected language")

    ents = GetSpacyData.GetEntities(
        doc
    )  # construct entities from text

    # To prevent appending challenges, the final JSON is created in GetEntities()
    # entMentions= GetSpacyData.entityMentionJson(ents)  #Returns JSON object containing an array of entity mentions
    await Db.InitializeIndexDB(
        "./Database/DB.db"
    )  # makes the DB containing the entities of KG
    # Returns JSON object containing an array of entity links
    entLinks = await entitylinkerFunc(
        ents
    )  # Returns JSON object containing an array of entity links

    entsJSON = GetSpacyData.BuildJSONFromEntities(
        entLinks,
        doc,
        "Artikel.txt"
    )

    with open("entity_mentions.json", "w", encoding="utf8") as entityJson:
        json.dump(entsJSON, entityJson, ensure_ascii=False, indent=4)