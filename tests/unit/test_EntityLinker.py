import sys

sys.path.append(".")

import pytest
from components.EntityLinker import entitylinkerFunc
from lib.Entity import Entity
from unittest.mock import patch


# Define a test case with a mock database and Entity instances
@pytest.mark.asyncio
async def test_entitylinkerFunc():
    # Mock the database Read and Insert methods
    async def mock_read(db_path, table, searchPred):
        if table == "EntityIndex":
            return [("1", "Entity1"), ("2", "Entity2")]
        return []

    async def mock_insert(db_path, table, entity_name):
        return None

    # Patch the Db.Read and Db.Insert functions with the mock functions
    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch(
            "components.EntityLinker.Db.Insert", side_effect=mock_insert
        ):
            # Create some Entity instances
            entMentions = [
                Entity("Entity1", 0, 6, "Sentence1", 0, 9, "PERSON", "Entity"),
                Entity("newEntity3", 0, 6, "Sentence2", 0, 9, "PERSON", "Entity"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions, db_path="DB_PATH")
            # Check the results
            assert len(entLinks) == 2

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity1"

            # Ensure the second mention creates a new entity
            assert entLinks[1].iri == "Entity1"


# Define a test case with a mock database and Entity instances
@pytest.mark.asyncio
async def test_entitylinkerFuncFindsCandidatesThatStartWithE():
    # Mock the database Read and Insert methods
    async def mock_read(db_path, table, searchPred):
        if table == "EntityIndex":
            return [("1", "Entity1")]
        return []

    async def mock_insert(db_path, table, entity_name):
        return None

    # Patch the Db.Read and Db.Insert functions with the mock functions
    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch(
            "components.EntityLinker.Db.Insert", side_effect=mock_insert
        ):
            # Create some Entity instances
            entMentions = [
                Entity("Entity1", 0, 6, "Sentence1", 0, 9, "PERSON", "Entity"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions, db_path="DB_PATH")
            # Check the results
            assert len(entLinks) == 1

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity1"

        # Define a test case with a mock database and Entity instances


@pytest.mark.asyncio
async def test_CheckIfSpaceHasBeenReplacedWithUnderscore():
    # Mock the database Read and Insert methods
    async def mock_read(db_path, table, searchPred):
        if table == "EntityIndex":
            return [("1", "Entity 1")]
        return []

    async def mock_insert(db_path, table, entity_name):
        return None

        # Patch the Db.Read and Db.Insert functions with the mock functions

    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch(
            "components.EntityLinker.Db.Insert", side_effect=mock_insert
        ):
            # Create some Entity instances
            entMentions = [
                Entity("Entity1", 0, 6, "Sentence1", 0, 9, "PERSON", "Entity"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions, db_path="DB_PATH")
            # Check the results
            assert len(entLinks) == 1

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity_1"


lastAddedID = 2


@pytest.mark.asyncio
async def test_entitylinkeraccuracy():
    # Mock the database Read and Insert methods
    mockDB = []
    mockDB.append((1, "Bob"))

    async def mock_read(dbPath, tableName, searchPred=None):
        if tableName == "EntityIndex" and searchPred is not None:
            # Filter and return all entries where mockDB[x][1] starts with searchPred
            filtered_entries = [
                (id, name)
                for id, name in mockDB
                if name.startswith(searchPred)
            ]
            return filtered_entries

        return mockDB

    async def mock_insert(db_path, table, queryInformation):
        global lastAddedID
        if table == "EntityIndex":
            mockDB.append((lastAddedID, queryInformation["entity"]))
            lastAddedID += 1
        return None

    # Patch the Db.Read and Db.Insert functions with the mock functions
    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch(
            "components.EntityLinker.Db.Insert", side_effect=mock_insert
        ):
            names_with_duplicates = [
                "Barrack Obama",
                "Barrack",
                "Johnathan",
                "John",
            ]
            # Create some Entity instances
            TestingDataset = {
                "test": [
                    Entity(name, 0, 6, "Sentence1", 0, 9, "PERSON", "Entity")
                    for name in names_with_duplicates
                ],
                "GoldStandardNames": [
                    "Barrack Obama",
                    "Barrack",
                    "Johnathan",
                    "John",
                ],
                "GoldStandardIRIs": [
                    "Barrack_Obama",
                    "Barrack_Obama",
                    "Johnathan",
                    "Johnathan",
                ],
            }

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(TestingDataset["test"], db_path="DB_PATH")
            for index, link in enumerate(entLinks):
                assert link.name == TestingDataset["GoldStandardNames"][index]
                assert link.iri == TestingDataset["GoldStandardIRIs"][index]
