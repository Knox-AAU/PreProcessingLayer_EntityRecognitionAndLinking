from components import *
from components.EntityLinker import entitylinkerFunc
import json, os
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

async def newFileCreated(file_path: str):
    await main(file_path)

dirWatcher = DirectoryWatcher(directory=DIRECTORY_TO_WATCH, async_callback=newFileCreated)

@app.on_event("startup")
async def startEvent():
    dirWatcher.start_watching()

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


@app.get("/entitymentions")
async def get_json(article: str = Query(..., title="Article Filename")):
    path = DIRECTORY_TO_WATCH + article
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Article not found")
    
    await main(path)  # Pass the article parameter to your main function
    with open("entity_mentions.json", "r") as entity_json:
        entity_mentions = json.load(entity_json)
        return entity_mentions


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


async def main(file_path: str = "Artikel.txt"):
    open("entity_mentions.json", "w").close()

    text = GetSpacyData.GetText(
        file_path
    )  # Takes in title of article. Gets article text in string format
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
        file_path
    )

    with open("entity_mentions.json", "w", encoding="utf8") as entityJson:
        json.dump(entsJSON, entityJson, ensure_ascii=False, indent=4)