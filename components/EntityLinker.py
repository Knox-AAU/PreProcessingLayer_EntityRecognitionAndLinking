from Levenshtein import distance
from components import Db
from lib.EntityLinked import EntityLinked


async def entitylinkerFunc(entMentions, threshold = 3):
    entLinks = []
    # for all mentions in the text
    for mention in entMentions:
        # find candidates from DB
        entsFromDb = await Db.Read('./Database/DB.db', "EntityIndex")

        # if no candidate is found, the entity is simply added to the DB (with a newly generated ID)
        if len(entsFromDb) == 0:
            entityIndex = await Db.Insert('./Database/DB.db', "EntityIndex", mention.name)
            entLinks.append(EntityLinked(mention, entityIndex))
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
            entityIndex = await Db.Insert('./Database/DB.db', "EntityIndex", mention.name)
            entLinks.append(EntityLinked(mention, entityIndex))
        else:
            entLinks.append(EntityLinked(mention, bestCandidate[0]))
    
    #print(entLinks)
    return entLinks
