from Levenshtein import distance
from components import Db
from lib.EntityLinked import EntityLinked


async def entitylinkerFunc(entMentions, threshold = 3):
    entLinks = []
    dbPath = "./Database/DB.db"
    tableName = "EntityIndex"
    #Sorting DB for optimization reasons
    await Db.SortDB(dbPath, tableName)
    # for all mentions in the text
    for mention in entMentions:
        # find candidates from DB
        entsFromDb = await Db.Read(dbPath, tableName, mention.name[0])

        # if no candidate is found, the entity is simply added to the DB (with a newly generated ID)
        if len(entsFromDb) == 0:
            await Db.Insert(dbPath, tableName, mention.name)
            entLinks.append(EntityLinked(mention, mention.name))
            continue

        smallestDistance = 100000
        bestCandidate = None
        # for each candidate, calculate the levenshtein distance between the mention and the candidate
        for candidate in entsFromDb:
            # Give each a ranking with the levenshtein distance
            #print("MENTION")
            #print(candidate[1])
            #print(mention)
            levenshteinDistance = distance(mention.name, candidate[1])
            #print("CANDIDATE RANKING")
            #print(levenshteinDistance)
            #print(candidate)

            # if the levenshtein distance is below a threshold, the candidate is added to the list of candidates
            if levenshteinDistance < threshold and levenshteinDistance < smallestDistance:
                smallestDistance = levenshteinDistance
                # return the best candidate
                bestCandidate = candidate

        #print("BEST CANDIDATE")
        #print(bestCandidate)

        # if the best candidate is above some threshold, add the link otherwise create a new entity in the DB
        if bestCandidate is None:
            await Db.Insert(dbPath, tableName, mention.name)
            entLinks.append(EntityLinked(mention, mention.name))
        else:
            entLinks.append(EntityLinked(mention, bestCandidate[1]))
    
    #print(entLinks)
    return entLinks
