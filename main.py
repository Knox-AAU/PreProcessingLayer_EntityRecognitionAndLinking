from typing import List
from components import *
from components.DbJSONAdapter import fetchAllEntityMentions, fetchEntityMentions, insertEntitiesInDb
from components.EntityLinker import entitylinkerFunc
import os
from lib.Exceptions.UndetectedLanguageException import (
    UndetectedLanguageException,
)
from lib.DirectoryWatcher import DirectoryWatcher
from langdetect import detect
from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="public")
app = FastAPI(title="API")

DIRECTORY_TO_WATCH = "data_from_A/"
DB_PATH = "./Database/DB.db"

async def newFileCreated(file_path: str):
    await processInput(file_path)

dirWatcher = DirectoryWatcher(directory=DIRECTORY_TO_WATCH, async_callback=newFileCreated)


@app.on_event("startup")
async def startEvent():
    dirWatcher.start_watching()

    await Db.InitializeIndexDB(
        DB_PATH
    )  # makes the DB containing the entities of KG
    


@app.on_event("shutdown")
def shutdown_event():
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

@app.get("/entitymentions/all")
async def get_all_json():
    return await fetchAllEntityMentions(DB_PATH, DIRECTORY_TO_WATCH)

@app.get("/entitymentions")
async def get_json(article: str = Query(..., title="Article Filename")):
    path = DIRECTORY_TO_WATCH + article
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Article not found")
    
    newFile = await processInput(path)
    return newFile

@app.post("/detectlanguage")
async def checklang(request: Request):
    data = await request.body()
    stringdata = str(data)
    print(len(stringdata))
    if len(stringdata) < 4:
        raise HTTPException(status_code=400, detail="Text is too short")

    language = detect(stringdata)

    return language


async def processInput(file_path: str = "Artikel.txt"):
    text = GetSpacyData.GetText(
        file_path
    )  # Takes in title of article. Gets article text in string format

    mentionsJSON = await fetchEntityMentions(DB_PATH, file_path, text)
    if len(mentionsJSON) > 0:
        return mentionsJSON

    doc = GetSpacyData.GetTokens(
        text
    )  # finds entities in text, returns entities in doc object

    text = GetSpacyData.GetText(
        file_path
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

    entLinks = await entitylinkerFunc(
        ents
    )  # Returns JSON object containing an array of entity links

    await insertEntitiesInDb(DB_PATH, file_path, entLinks)
    return await fetchEntityMentions(DB_PATH, file_path, text)
