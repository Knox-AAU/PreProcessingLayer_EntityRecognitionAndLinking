# Our part of the pipeline
### (also available at: [http://wiki.knox.aau.dk/en/entity-extraction](http://wiki.knox.aau.dk/en/entity-extraction))

Our part of the pipeline is concerned with Entity Recognition and Entity Linking. This solution utilizes the [SpaCy](https://spacy.io/) library to perform Entity Recognition, and the [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/) library for the entity linking. 

> Every following section describes this pipeline *in order*, but first a visual overview.

## Overview
![](img/KNOX_component_diagram-B.drawio.svg)

## How to get started
See the [Getting started](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/gettingstarted.md) guide.

## The input that the solution takes
See the [input](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/our-part-of-the-pipeline/pipeline-input.md) explanation

## Entity Recognition
Check out the [Entity Recognition documentation](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/entityrecognition.md)

## Entity Linking
Check out the [Entity Linker documentation](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/entitylinker.md)

## The output it produces
See the [output](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/our-part-of-the-pipeline/pipeline-output.md) explanation


## Other components
- The [DirectoryWatcher](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/DirectoryWatcher.md)
- The [Database](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/database.md)
- The [APIs](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/api.md)
- The [Language Detector](https://pypi.org/project/langdetect/)

## Future work
