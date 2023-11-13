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
    async def mock_read(db_path, table):
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
                Entity("Entity1", 0, 6, "file1"),
                Entity("newEntity3", 0, 6, "file2"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions)
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
    async def mock_read(db_path, table):
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
                Entity("Entity1", 0, 6, "file1"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions)
            # Check the results
            assert len(entLinks) == 1

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity1"

        # Define a test case with a mock database and Entity instances


@pytest.mark.asyncio
async def test_CheckIfSpaceHasBeenReplacedWithUnderscore():
    # Mock the database Read and Insert methods
    async def mock_read(db_path, table):
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
                Entity("Entity1", 0, 6, "file1"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions)
            # Check the results
            assert len(entLinks) == 1

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity_1"


lastAddedID = 2


@pytest.mark.asyncio
async def test_entitylinkeraccuracy():
    print("TESTING ACCURACY")
    # Mock the database Read and Insert methods
    mockDB = []
    mockDB.append((1, "Bob"))

    async def mock_read(db_path, table):
        if table == "EntityIndex":
            return mockDB
        return []

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
                "John",
                "Alice",
                "Bob",
                "Eva",
                "Charlie",
                "Olivia",
                "David",
                "Sophia",
                "Michael",
                "Emma",
                "Daniel",
                "Ava",
                "William",
                "Mia",
                "Alexander",
                "Emily",
                "James",
                "Abigail",
                "Benjamin",
                "Harper",
                "Liam",
                "Ella",
                "Henry",
                "Grace",
                "Christopher",
                "Avery",
                "Andrew",
                "Scarlett",
                "Emma",
                "Zoe",
                "Nathan",
                "Madison",
                "Elijah",
                "Lily",
                "Ethan",
                "Chloe",
                "Isaac",
                "Aria",
                "Ryan",
                "Hannah",
                "Matthew",
                "Amelia",
                "Nicholas",
                "Sofia",
                "Joseph",
                "Addison",
                "Luke",
                "Aubrey",
                "Jack",
                "Lillian",
                "Samuel",
                "Natalie",
                "Sebastian",
                "Evelyn",
                "Logan",
                "Victoria",
                "Lucas",
                "Aaliyah",
                "Jackson",
                "Brooklyn",
                "Owen",
                "Layla",
                "Caleb",
                "Scarlet",
                "Gabriel",
                "Aria",
                "Dylan",
                "Alexa",
                "Mason",
                "Katherine",
                "Isaiah",
                "Zoey",
                "Brandon",
                "Audrey",
                "Julian",
                "Bella",
                "Cameron",
                "Skylar",
                "Johnathan",
                "Claire",
                "Wyatt",
                "Alyssa",
                "Connor",
                "Peyton",
                "Isabel",
                "Lauren",
                "Alex",
                "Sophie",
                "Tyler",
                "Mackenzie",
                "John",
                "Emma",
                "Sophia",
                "Liam",
                "Olivia",
                "Mia",
                "Noah",
                "Eva",
                "Ava",
                "Isabella",
            ]
            # Create some Entity instances
            TestingDataset = {
                "test": [
                    Entity(name, 0, 6, "file")
                    for name in names_with_duplicates
                ],
                "GoldStandard": [
                    "John",
                    "Alice",
                    "Bob",
                    "Eva",
                    "Charlie",
                    "Olivia",
                    "David",
                    "Sophia",
                    "Michael",
                    "Emma",
                    "Daniel",
                    "Ava",
                    "William",
                    "Mia",
                    "Alexander",
                    "Emily",
                    "James",
                    "Abigail",
                    "Benjamin",
                    "Harper",
                    "Liam",
                    "Ella",
                    "Henry",
                    "Grace",
                    "Christopher",
                    "Avery",
                    "Andrew",
                    "Scarlett",
                    "Emma",
                    "Zoe",
                    "Nathan",
                    "Madison",
                    "Elijah",
                    "Lily",
                    "Ethan",
                    "Chloe",
                    "Isaac",
                    "Aria",
                    "Ryan",
                    "Hannah",
                    "Matthew",
                    "Amelia",
                    "Nicholas",
                    "Sofia",
                    "Joseph",
                    "Addison",
                    "Luke",
                    "Aubrey",
                    "Jack",
                    "Lillian",
                    "Samuel",
                    "Natalie",
                    "Sebastian",
                    "Evelyn",
                    "Logan",
                    "Victoria",
                    "Lucas",
                    "Aaliyah",
                    "Jackson",
                    "Brooklyn",
                    "Owen",
                    "Layla",
                    "Caleb",
                    "Scarlet",
                    "Gabriel",
                    "Aria",
                    "Dylan",
                    "Alexa",
                    "Mason",
                    "Katherine",
                    "Isaiah",
                    "Zoey",
                    "Brandon",
                    "Audrey",
                    "Julian",
                    "Bella",
                    "Cameron",
                    "Skylar",
                    "Johnathan",
                    "Claire",
                    "Wyatt",
                    "Alyssa",
                    "Connor",
                    "Peyton",
                    "Isabel",
                    "Lauren",
                    "Alex",
                    "Sophie",
                    "Tyler",
                    "Mackenzie",
                    "John",
                    "Emma",
                    "Sophia",
                    "Liam",
                    "Olivia",
                    "Mia",
                    "Noah",
                    "Eva",
                    "Ava",
                    "Isabella",
                ],
            }

            # Call the entitylinkerFunc
            print("calling entitylinker from accuracy test")
            entLinks = await entitylinkerFunc(TestingDataset["test"])
            print("linker done")
            for index, link in enumerate(entLinks):
                assert link.iri == TestingDataset["GoldStandard"][index]
