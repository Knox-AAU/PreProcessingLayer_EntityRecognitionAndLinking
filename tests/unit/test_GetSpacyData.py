import sys
import pytest

sys.path.append(".")
from components import GetSpacyData
from lib.Entity import Entity


# Test that GetText returns the correct text from the file
def test_GetText_fileExists():
    with open("test_article_file.txt", "w") as testFile:
        testFile.write("This is a testfile")

    testText = GetSpacyData.GetText("test_article_file.txt")
    assert testText == "This is a testfile"


# Test that GetText returns an error if the file does not exist
def test_GetText_fileNonExistent():
    with pytest.raises(FileNotFoundError):
        testTet = GetSpacyData.GetText("NonExistentFile.txt")


# Testing that GetTokens returns the correct number of entities
# and the needed data for the entities
def test_GetTokens():
    testDoc = GetSpacyData.GetTokens("Drake kan godt lide at sutte på lilletær")
    assert len(testDoc.ents) == 2
    assert testDoc.ents[0].text == "Drake"
    assert testDoc.ents[0].start_char == 0
    assert testDoc.ents[0].end_char == 5
    assert testDoc.ents[1].text == "lilletær"
    assert testDoc.ents[1].start_char == 32
    assert testDoc.ents[1].end_char == 40


# Testing that GetEntities returns all entities and their indexes
def test_GetEntities():
    docFile = type('obj', (object,), {
        "ents": [
            type('obj', (object,), {
                "sent": type('obj', (object,), {
                    "text": "Drake kan godt lide at sutte på lilletær",
                    "start_char": 0,
                    "end_char": 40
                }),
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
                "text": "Buddyguy",
                "start_char": 6,
                "end_char": 14
            })
        ]
    })()

    filename = "Nordjyske"

    # Ensure the structure of docFile matches the expected format

    entities = GetSpacyData.GetEntities(docFile, filename)
    print(entities)
    assert entities["sentences"][0]["sentence"] == "Drake kan godt lide at sutte på lilletær"
    assert entities["sentences"][0]["entityMentions"][0]["name"] == "Drake"
    assert entities["sentences"][0]["entityMentions"][0]["startIndex"] == 0
    assert entities["sentences"][0]["entityMentions"][0]["endIndex"] == 5
    assert entities["fileName"] == "Nordjyske"

    assert entities["sentences"][1]["sentence"] == "Hello Buddyguy"
    assert entities["sentences"][1]["entityMentions"][0]["name"] == "Buddyguy"
    assert entities["sentences"][1]["entityMentions"][0]["startIndex"] == 6
    assert entities["sentences"][1]["entityMentions"][0]["endIndex"] == 14
    assert entities["fileName"] == "Nordjyske"