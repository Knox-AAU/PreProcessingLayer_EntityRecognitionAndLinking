import pytest
from fastapi.testclient import TestClient
import sys

sys.path.append(".")
from main import app


@pytest.mark.asyncio
async def test_SlashEntityMentionsIsUp():
    with TestClient(app) as client:
        res = client.get("/entitymentions")
        assert res.status_code == 200
        client.__exit__
        client.close()


@pytest.mark.asyncio
async def test_SlashEntityMentionsReturnsJsonArray():
    with TestClient(app) as client:
        res = client.get("/entitymentions")
        assert type(res.json()) == list
        assert type(res.json()[0]) == dict
        client.__exit__
        client.close()
