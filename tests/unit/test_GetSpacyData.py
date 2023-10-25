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
    docFile = type(
        "obj",
        (object,),
        {
            "ents": [
                type(
                    "obj", (object,), {"text": "Drake", "start_char": 0, "end_char": 5}
                ),
                type(
                    "obj",
                    (object,),
                    {"text": "Buddyguy", "start_char": 6, "end_char": 14},
                ),
            ]
        },
    )()
    print(docFile.ents[0].text)

    filename = "Nordjyske"

    entities = GetSpacyData.GetEntities(docFile, filename)
    assert entities[0].name == "Drake"
    assert entities[0].startIndex == 0
    assert entities[0].endIndex == 5
    assert entities[0].fileName == "Nordjyske"

    assert entities[1].name == "Buddyguy"
    assert entities[1].startIndex == 6
    assert entities[1].endIndex == 14
    assert entities[1].fileName == "Nordjyske"


# test that entityMentionsJson is correctly creating JSON array
def test_entityMentionJson():
    ents = [Entity("Drake", 0, 5, "Nordjyske"), Entity("Buddyguy", 6, 14, "Nordjyske")]
    JSONArray = GetSpacyData.entityMentionJson(ents)
    assert JSONArray == [
        {"name": "Drake", "startIndex": 0, "endIndex": 5, "fileName": "Nordjyske"},
        {"name": "Buddyguy", "startIndex": 6, "endIndex": 14, "fileName": "Nordjyske"},
    ]
