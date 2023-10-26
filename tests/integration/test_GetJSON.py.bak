from email.mime import base
from typing import AsyncIterator
from fastapi import FastAPI
from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
from asgi_lifespan import LifespanManager
import sys

import pytest_asyncio

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
