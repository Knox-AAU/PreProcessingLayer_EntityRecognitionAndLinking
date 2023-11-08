# API

## /entitymentions <sup><span style="color:lightgreen">GET</span></sup>

The `/entitymentions` endpoint is a <span style="color:lightgreen">**GET**</span> endpoint. When doing a <span style="color:lightgreen">**GET**</span> request to the endpoint, a JSON Array is returned containing all the currently known entitymentions, their indexes and the file they originate from. The format of the JSON array is formatted as follows:

```JSON
[
    {
        "name": "ENTITY MENTION",
        "startIndex": INT,
        "endIndex":INT,
        "fileName":"FILENAME.EXTENSION"
    },
    {
        "name": "ENTITY MENTION",
        "startIndex": INT,
        "endIndex":INT,
        "fileName":"FILENAME.EXTENSION"
    }
]
```

### Example Output

Here is an example of an output from the endpoint. For simplification, only a single file has been processed by the Entity Recognizer and Linker, and just a few of the found entity mentions is shown below:

```JSON
[
    {
        "name": "Martin Kjærs",
        "startIndex": 28,
        "endIndex": 40,
        "fileName": "Artikel.txt"
    },
    {
        "name": "Region Nordjylland",
        "startIndex": 100,
        "endIndex": 118,
        "fileName": "Artikel.txt"
    },
    {
        "name": "Aalborg",
        "startIndex": 285,
        "endIndex": 292,
        "fileName": "Artikel.txt"
    }
]
```


## articlename/entities <sup><span style="color:lightgreen">GET</span></sup>

The `articlename/entities` endpoint is a <span style="color:lightgreen">**GET**</span> endpoint. The articlename in the url has to replaced with a name of an article including .txt. When doing a GET request to the endpoint, a JSON Array is returned containing the currently known entitymentions found in the given article name including their indexes. The format of the JSON array is formatted as follows:

```JSON
[
    {
        "name": "ENTITY MENTION",
        "startIndex": INT,
        "endIndex":INT,
        "fileName":"FILENAME.EXTENSION"
    },
    {
        "name": "ENTITY MENTION",
        "startIndex": INT,
        "endIndex":INT,
        "fileName":"FILENAME.EXTENSION"
    }
]
```

### Example Output

Here is an example of an output from the endpoint when getting for  <span style="color:lightgreen">Artikel.txt/entities</span>. For simplification, only a single file has been processed by the Entity Recognizer and Linker, and just a few of the found entity mentions is shown below:

```JSON
[
    {
        "name": "Martin Kjærs",
        "startIndex": 28,
        "endIndex": 40,
        "fileName": "Artikel.txt"
    },
    {
        "name": "Region Nordjylland",
        "startIndex": 100,
        "endIndex": 118,
        "fileName": "Artikel.txt"
    },
    {
        "name": "Aalborg",
        "startIndex": 285,
        "endIndex": 292,
        "fileName": "Artikel.txt"
    }
]
```
