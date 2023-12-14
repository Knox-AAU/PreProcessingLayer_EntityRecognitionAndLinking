# Entity Linking

Entity linking in the knox project is performed using a string comparison algorithm to determine the closest comparable entity.

## How it is linked

Linking entities to eachother happens through IRI's. An entity is given a unique IRI. Whenever an entity is identified as being the same entity as another, the entitiy is linked to the same IRI.

## Comparison Algorithm

Currently, KNOX utilizes the FuzzyWuzzy library for python to determine candidates to link an entity to. FuzzyWuzzy is build upon the Levenshtein algorithm, which works by looking at how many modifications is needed to change one string to another. The less modification needed to alter the string to be equal to the other, the closer the string is. Using FuzzyWuzzy we naively determine entities to link to. It is therefore not the optimal solution, and this should be changed later on.

## Performing entity linking on an input

```PYTHON
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
```

Entity linking is performed using the above function. The function takes in a list of entities which would be found in a new article processed in the KNOX pipeline. It then iterates through all found entities and sort out all that is of type LITERAL.

After this, a list of potential matches is then found from the database, that all start the string of the entity to be linked.

FuzzyWuzzy is then used to find the best candidate.

<div style="text-align: right">
    Up next:
    <br>
    <a href="https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/our-part-of-the-pipeline/pipeline-output.md">Entity Linker</a>
    <span class="pagination_icon__3ocd0"><svg class="with-icon_icon__MHUeb" data-testid="geist-icon" fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24" style="color:currentColor;width:11px;height:11px"><path d="M9 18l6-6-6-6"></path></svg></span>
</div>
