from typing import List
from Levenshtein import distance
from components import Db
from lib.EntityLinked import EntityLinked
from lib.Entity import Entity
from fuzzywuzzy import process


async def entitylinkerFunc(
    entities: List[Entity], db_path: str, threshold: int = 80
):
    iri_dict = {}
    linked_entities = []

    for entity in entities:
        if entity.type == "Literal":
            linked_entities.append(EntityLinked(entity, ""))
            continue

        # Use the Read function to get all entities starting with the same name
        potential_matches = await Db.Read(
            db_path, "EntityIndex", searchPred=entity.name
        )

        if potential_matches:
            names_only = [match[1] for match in potential_matches]

            # Use fuzzy matching to find the best candidate
            best_candidate_name, similarity = process.extractOne(
                entity.name, names_only
            )

            # Check if the similarity is above the threshold
            if similarity >= threshold:
                iri = best_candidate_name.replace(" ", "_")
                iri_dict[entity] = EntityLinked(entity, iri)
            else:
                # If no match above the threshold, add to the result and update the database
                iri = entity.name.replace(" ", "_")
                iri_dict[entity] = EntityLinked(entity, iri)
                await Db.Insert(
                    db_path,
                    "EntityIndex",
                    queryInformation={"entity": entity.name},
                )
        else:
            # If not found in the database, add to the result and update the database
            iri = entity.name.replace(" ", "_")
            iri_dict[entity] = EntityLinked(entity, iri)
            await Db.Insert(
                db_path,
                "EntityIndex",
                queryInformation={"entity": entity.name},
            )

    # Convert the result to an array of EntityLinked
    for linked_entity in iri_dict.values():
        linked_entities.append(linked_entity)

    return linked_entities
