from multiprocessing import Process
import sys

from typing import Type

sys.path.append(".")
import pytest, main, uvicorn, fastapi.testclient

client = fastapi.testclient.TestClient(main.app)


def run_server():
    uvicorn.run(main.app)


def test_SlashEntityMentionsIsUp():
    res = client.get("/entitymentions")
    assert res.status_code == 200


def test_SlashEntityMentionsReturnsJsonArray():
    res = client.get("/entitymentions")
    assert type(res.json()) == list
    assert type(res.json()[0]) == dict
