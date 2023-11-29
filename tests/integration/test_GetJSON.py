import pytest
from fastapi.testclient import TestClient
import sys
from unittest.mock import patch
import os


sys.path.append(".")
from main import app, DIRECTORY_TO_WATCH
import os

directory_path = "data_from_A/"
file_path = "data_from_A/test.txt"
text_to_write = "Since the sudden exit of the controversial CEO Martin Kjær last week, both he and the executive board in Region North Jutland have been in hiding."

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

# Create the file if it doesn't exist and write text into it
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write(text_to_write)

@pytest.mark.asyncio
async def test_SlashEntityMentionsIsUp():
    with patch('main.DIRECTORY_TO_WATCH', directory_path):
        with TestClient(app) as client:
            yield client
            res = client.get("/entitymentions?article=test.txt")
            assert res.status_code == 200
            client.__exit__
            client.close()


@pytest.mark.asyncio
async def test_SlashEntityMentionsAllReturnsJsonArray():
    with TestClient(app) as client:
        yield client
        res = client.get("/entitymentions/all")
        print(type(res.json()))
        assert type(res.json()) == list
        assert type(res.json()[0]) == dict
        client.__exit__
        client.close()

@pytest.mark.asyncio
async def test_SlashEntityMentionsReturnsJson():
    with patch('main.DIRECTORY_TO_WATCH', directory_path):
        with TestClient(app) as client:
            yield client
            res = client.get("/entitymentions?article=test.txt")
            assert type(res.json()) == dict
            client.__exit__
            client.close()