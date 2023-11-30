import sys
from fastapi.testclient import TestClient
import pytest
from main import app
from langdetect import detect

def test_lang_da():
   assert detect("hej, jeg bor i et hus som ligger i Aalborg.") == "da"


def test_lang_en():
   assert detect("My name is Mike Oxlong. I live in Alabama which is located in the US.") == "en"