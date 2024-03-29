from components import *
from components.EntityLinker import entitylinkerFunc
import json, os, time, string
from lib.Exceptions.UndetectedLanguageException import (
    UndetectedLanguageException,
)
from lib.DirectoryWatcher import DirectoryWatcher
from langdetect import detect
from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from dotenv import load_dotenv
import uvicorn

templates = Jinja2Templates(directory="public")
app = FastAPI(title="API")

load_dotenv()

DIRECTORY_TO_WATCH = str(os.getenv("DIRECTORY_TO_WATCH"))
PIPELINE_C_URL = str(os.getenv("PIPELINE_C_URL"))
PIPELINE_C_AUTHORIZATION = str(os.getenv("PIPELINE_C_AUTHORIZATION"))
ACCESS_API_AUTHORIZATION = str(os.getenv("ACCESS_API_AUTHORIZATION"))
DB_PATH = str(os.getenv("DB_PATH"))

async def newFileCreated(file_path: str):
    try:
        newFileProcessed = await processInput(file_path)
        print(newFileProcessed)
        Headers = { "Authorization" : PIPELINE_C_AUTHORIZATION, "Access-Authorization": ACCESS_API_AUTHORIZATION }
        r = requests.post(PIPELINE_C_URL, json=[newFileProcessed], headers=Headers)
        print(r.content)
        print(r)
        print(r.json())
    except Exception as e:
        #Server does not need to freeze everytime an exeption is thrown
        print(f"An exception occurred: {str(e)}")
        return {"error": str(e)}

dirWatcher = DirectoryWatcher(
    directory=DIRECTORY_TO_WATCH, async_callback=newFileCreated
)

@app.on_event("startup")
async def startEvent():
    if not os.path.exists(DIRECTORY_TO_WATCH):
        os.mkdir(DIRECTORY_TO_WATCH)

    if os.path.exists(DIRECTORY_TO_WATCH):
        dirWatcher.start_watching()


@app.on_event("shutdown")
def shutdown_event():
    if os.path.exists(DIRECTORY_TO_WATCH):
        dirWatcher.stop_watching()


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/entitymentions/all")
async def get_all_json():
    if not os.path.exists("entity_mentions.json"):
        raise HTTPException(status_code=404, detail="mentions not found")

    with open("entity_mentions.json", "r") as entity_json:
        entity_mentions = json.load(entity_json)
        return entity_mentions


@app.get("/entitymentions")
async def get_json(article: str = Query(..., title="Article Filename")):
    path = DIRECTORY_TO_WATCH + article
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Article not found")
    try:
        newFile = await processInput(path)
    except Exception as e:
        #Server does not need to freeze everytime an exeption is thrown
        print(f"An exception occurred: {str(e)}")
        return {"error": str(e)}
    return newFile

@app.post("/detectlanguage")
async def checklang(request: Request):
    data = await request.body()
    stringdata = str(data)
    if len(stringdata) < 4:
        raise HTTPException(status_code=400, detail="Text is too short")

    language = detect(stringdata)

    return language

async def processInput(file_path: str = "Artikel.txt"):
    text = GetSpacyData.GetText(
        file_path
    )  # Takes in title of article. Gets article text in string format
    
    try:
        doc = GetSpacyData.GetTokens(
            text
        )  # finds entities in text, returns entities in doc object
    except UndetectedLanguageException:
        raise HTTPException(status_code=400, detail="Undetected language")

    ents = GetSpacyData.GetEntities(doc)  # construct entities from text

    await Db.InitializeIndexDB(
        DB_PATH
    )  # makes the DB containing the entities of KG
    # Returns JSON object containing an array of entity links

    entLinks = await entitylinkerFunc(
        ents,
        DB_PATH
    )  # Returns JSON object containing an array of entity links

    entsJSON = GetSpacyData.BuildJSONFromEntities(entLinks, doc, file_path)

    with open("entity_mentions.json", "w", encoding="utf8") as entityJson:
        json.dump(entsJSON.allFiles, entityJson, ensure_ascii=False, indent=4)

    return entsJSON.newFile

# Allows this file to be run like so: "python main.py"
# Useful for debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)