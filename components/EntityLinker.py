from Levenshtein import distance
from components import Db
from lib.EntityLinked import EntityLinked
from lib.Entity import Entity
from fuzzywuzzy import fuzz


def GetAllEntities(entityMentions):
    allEntities = []
    fileName = ""
    for file in entityMentions:
        fileName = file["fileName"]
        for sentence in file["sentences"]:
            for entity in sentence["entityMentions"]:
                newEntity = Entity(
                    name=entity["name"],
                    startIndex=entity["startIndex"],
                    endIndex=entity["endIndex"],
                    sentence=sentence["sentence"],
                    sentenceStartIndex=sentence["sentenceStartIndex"],
                    sentenceEndIndex=sentence["sentenceEndIndex"],
                    label=entity["label"],
                    type=entity["type"],
                )
                allEntities.append(newEntity)
    return allEntities


async def entitylinkerFunc(entities, threshold=80):
    iri_dict = {}
    linked_entities = []
    db_path = "./Database/DB.db"
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
            # Sort the potential matches by length difference and select the first one
            best_candidate_name = min(
                names_only,
                key=lambda x: abs(len(x[0]) - len(entity.name)),
            )
            iri = best_candidate_name.replace(" ", "_")
            iri_dict[entity] = EntityLinked(entity, iri)
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
