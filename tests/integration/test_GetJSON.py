import pytest
from fastapi.testclient import TestClient
import sys
from unittest.mock import patch

sys.path.append(".")
from main import app, DIRECTORY_TO_WATCH


@pytest.mark.asyncio
async def test_SlashEntityMentionsIsUp():
    with patch('main.DIRECTORY_TO_WATCH', 'data_from_A/'):
        with TestClient(app) as client:
            res = client.get("/entitymentions?article=test.txt")
            assert res.status_code == 200
            client.__exit__
            client.close()


@pytest.mark.asyncio
async def test_SlashEntityMentionsAllReturnsJsonArray():
    with TestClient(app) as client:
        res = client.get("/entitymentions/all")
        print(type(res.json()))
        assert type(res.json()) == list
        assert type(res.json()[0]) == dict
        client.__exit__
        client.close()

@pytest.mark.asyncio
async def test_SlashEntityMentionsReturnsJson():
    with patch('main.DIRECTORY_TO_WATCH', 'data_from_A/'):
        with TestClient(app) as client:
            res = client.get("/entitymentions?article=test.txt")
            assert type(res.json()) == dict
            client.__exit__
            client.close()