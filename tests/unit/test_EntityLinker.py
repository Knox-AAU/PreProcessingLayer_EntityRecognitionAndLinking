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
    async def mock_read(db_path, table, predicate):
        if table == "EntityIndex":
            return [("1", "Entity1"), ("2", "Entity2")]
        return []

    async def mock_insert(db_path, table, entity_name):
        return None

    # Patch the Db.Read and Db.Insert functions with the mock functions
    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch("components.EntityLinker.Db.Insert", side_effect=mock_insert):
            # Create some Entity instances
            entMentions = [
                Entity("Entity1", 0, 6, "file1"),
                Entity("newEntity3", 0, 6, "file2"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions, threshold=5)
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
    async def mock_read(db_path, table, predicate):
        if table == "EntityIndex":
            return [("1", "Entity1")]
        return []

    async def mock_insert(db_path, table, entity_name):
        return None 

    # Patch the Db.Read and Db.Insert functions with the mock functions
    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch("components.EntityLinker.Db.Insert", side_effect=mock_insert):
            # Create some Entity instances
            entMentions = [
                Entity("Entity1", 0, 6, "file1"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions, threshold=3)
            # Check the results
            assert len(entLinks) == 1

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity1"
            
            
        # Define a test case with a mock database and Entity instances
@pytest.mark.asyncio
async def test_CheckIfSpaceHasBeenReplacedWithUnderscore():
    # Mock the database Read and Insert methods
    async def mock_read(db_path, table, predicate):
        if table == "EntityIndex":
            return [("1", "Entity 1")]
        return []

    async def mock_insert(db_path, table, entity_name):
        return None     
        
        # Patch the Db.Read and Db.Insert functions with the mock functions
    with patch("components.EntityLinker.Db.Read", side_effect=mock_read):
        with patch("components.EntityLinker.Db.Insert", side_effect=mock_insert):
            # Create some Entity instances
            entMentions = [
                Entity("Entity 1", 0, 6, "file 1"),
            ]

            # Call the entitylinkerFunc
            entLinks = await entitylinkerFunc(entMentions, threshold=3)
            # Check the results
            assert len(entLinks) == 1

            # Ensure the first mention links to an existing entity
            assert entLinks[0].iri == "Entity_1"