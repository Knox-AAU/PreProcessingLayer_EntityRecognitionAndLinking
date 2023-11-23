import sys
import pytest

from lib import EntityLinked

sys.path.append(".")
from components import GetSpacyData
from lib.Entity import Entity
from lib.EntityLinked import EntityLinked


# Test that GetText returns the correct text from the file
def test_GetText_fileExists():
    with open("test_article_file.txt", "w") as testFile:
        testFile.write("This is a testfile")

    testText = GetSpacyData.GetText("test_article_file.txt")
    assert testText == "This is a testfile"


# Test that GetText returns an error if the file does not exist
def test_GetText_fileNonExistent():
    with pytest.raises(FileNotFoundError):
        GetSpacyData.GetText("NonExistentFile.txt")


# Testing that GetTokens returns the correct number of entities
# and the needed data for the entities
def test_GetTokens():
    testDoc = GetSpacyData.GetTokens("Drake likes to suck the toes of Donald Trump")
    assert len(testDoc.ents) == 2
    assert testDoc.ents[0].text == "Drake"
    assert testDoc.ents[0].start_char == 0
    assert testDoc.ents[0].end_char == 5
    assert testDoc.ents[1].text == "Donald Trump"
    assert testDoc.ents[1].start_char == 32
    assert testDoc.ents[1].end_char == 44


# Testing that GetEntities returns all entities and their indexes
@pytest.mark.asyncio
def test_GetEntities():
    docFile = type('obj', (object,), {
        "ents": [
            type('obj', (object,), {
                "sent": type('obj', (object,), {
                    "text": "Drake is a music artist",
                    "start_char": 0,
                    "end_char": 40
                }),
                "label_": "PERSON",
                "text": "Drake",
                "start_char": 0,
                "end_char": 5
            }),
            type('obj', (object,), {
                "sent": type('obj', (object,), {
                    "text": "Hello Buddyguy",
                    "start_char": 0,
                    "end_char": 14
                }),
                "label_": "PERSON",
                "text": "Buddyguy",
                "start_char": 6,
                "end_char": 14
            })
        ]
    })()

    filename = "Testing2023"

    # Ensure the structure of docFile matches the expected format

    entities = GetSpacyData.GetEntities(docFile)

    entLinks = []
    for entity in entities:
        entLinks.append(
            EntityLinked(
                entity,
                "knox.aau.dk/some_iri"
            )
        )

    entsJSON = GetSpacyData.BuildJSONFromEntities(
        entLinks,
        docFile,
        filename
    )

    testIndex = 0
    for i in range(len(entsJSON)):
        if entsJSON[i]["fileName"] == "Testing2023":
            testIndex = i
            break

    assert entsJSON[testIndex]["sentences"][0]["sentence"] == "Drake is a music artist" 
    assert entsJSON[testIndex]["sentences"][0]["entityMentions"][0]["name"] == "Drake"
    assert entsJSON[testIndex]["sentences"][0]["entityMentions"][0]["startIndex"] == 0
    assert entsJSON[testIndex]["sentences"][0]["entityMentions"][0]["endIndex"] == 5
    assert entsJSON[testIndex]["fileName"] == "Testing2023"

    assert entsJSON[testIndex]["sentences"][1]["sentence"] == "Hello Buddyguy"
    assert entsJSON[testIndex]["sentences"][1]["entityMentions"][0]["name"] == "Buddyguy"
    assert entsJSON[testIndex]["sentences"][1]["entityMentions"][0]["startIndex"] == 6
    assert entsJSON[testIndex]["sentences"][1]["entityMentions"][0]["endIndex"] == 14
    assert entsJSON[testIndex]["fileName"] == "Testing2023"