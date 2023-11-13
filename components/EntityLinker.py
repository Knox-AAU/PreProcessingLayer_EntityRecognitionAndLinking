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
                    fileName=fileName,
                )
                allEntities.append(newEntity)
    print(allEntities)
    return allEntities


# async def entitylinkerFunc(entMentions, threshold=3):
#     entLinks = []
#     dbPath = "./Database/DB.db"
#     tableName = "EntityIndex"
#     # Sorting DB for optimization reasons
#     # for all mentions in the text
#     for mention in entMentions:
#         # find candidates from DB
#         predicate = mention.name
#         predicate = predicate[0]
#         entsFromDb = await Db.Read(dbPath, tableName, predicate)

#         # if no candidate is found, the entity is simply added to the DB (with a newly generated ID)
#         if len(entsFromDb) == 0:
#             await Db.Insert(
#                 dbPath, tableName, queryInformation={"entity": mention.name}
#             )
#             entLinks.append(EntityLinked(mention, mention.name))
#             continue

#         smallestDistance = 100000
#         bestCandidate = None
#         # for each candidate, calculate the levenshtein distance between the mention and the candidate
#         for candidate in entsFromDb:
#             # Give each a ranking with the levenshtein distance
#             # print("MENTION")
#             # print(candidate[1])
#             # print(mention)
#             levenshteinDistance = distance(mention.name, candidate[1])
#             # print("CANDIDATE RANKING")
#             # print(levenshteinDistance)
#             # print(candidate)

#             # if the levenshtein distance is below a threshold, the candidate is added to the list of candidates
#             if (
#                 levenshteinDistance < threshold
#                 and levenshteinDistance < smallestDistance
#             ):
#                 smallestDistance = levenshteinDistance
#                 # return the best candidate
#                 bestCandidate = candidate

#         # print("BEST CANDIDATE")
#         # print(bestCandidate)

#         # if the best candidate is above some threshold, add the link otherwise create a new entity in the DB
#         if bestCandidate is None:
#             await Db.Insert(
#                 dbPath, tableName, queryInformation={"entity": mention.name}
#             )
#             entLinks.append(EntityLinked(mention, mention.name))
#         else:
#             entLinks.append(EntityLinked(mention, bestCandidate[1]))

#     # print(entLinks)
#     return entLinks


async def entitylinkerFunc(entities):
    linked_entities = []
    dbPath = "./Database/DB.db"
    tableName = "EntityIndex"
    knowledge_base = await Db.Read(dbPath, tableName)

    for entity in entities:
        entity_text = entity.name

        # Case-insensitive matching and approximate matching (fuzzy matching)
        matches = [
            key
            for key in knowledge_base
            if fuzz.token_sort_ratio(entity_text.lower(), key[1].lower()) > 80
        ]

        if matches:
            best_match = max(
                matches,
                key=lambda x: fuzz.token_sort_ratio(
                    entity_text.lower(), x[1].lower()
                ),
            )
            print(best_match)

            kb_entry_id = best_match[0]
            kb_entry = knowledge_base[kb_entry_id - 1]

            if kb_entry:
                # Check if the entity is already in linked_entities
                entity_exists = any(
                    linked_entity.id == kb_entry_id
                    for linked_entity in linked_entities
                )

                if entity_exists:
                    # Update the existing entry with the discovered IRI
                    for linked_entity in linked_entities:
                        if linked_entity.id == kb_entry_id:
                            linked_entity.iri = entity.name
                else:
                    # Add a new entry if the entity is not in linked_entities
                    linked_entities.append(
                        EntityLinked(entity, iri=entity.name, id=kb_entry_id)
                    )
            else:
                # Add a new entry if the entity is unknown
                linked_entities.append(
                    EntityLinked(entity, iri="Unknown Entity Mention", id=None)
                )
        else:
            # Handle the case when no match is found
            linked_entities.append(
                EntityLinked(entity, iri="Unknown Entity Mention", id=None)
            )

    return linked_entities
