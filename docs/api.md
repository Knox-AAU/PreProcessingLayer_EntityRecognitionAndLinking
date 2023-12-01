# API

## /entitymentions <sup><span style="color:lightgreen">GET</span></sup>
### Parameters
| Parameter | Type   | Description      |
|-----------|--------|------------------|
| `article` | STRING | The article path |

The `/entitymentions` endpoint is a <span style="color:lightgreen">**GET**</span> endpoint. When doing a <span style="color:lightgreen">**GET**</span> request to the endpoint, a JSON Array is returned containing all the currently known entitymentions, their indexes, type, label, iri and the file they originate from. The JSON array is formatted as follows:

```JSON
{
    "fileName": STRING,
    "language": STRING,
    "sentences": [
        {
            "sentence": STRING,
            "sentenceStartIndex": INT,
            "sentenceEndIndex": INT,
            "entityMentions": [
                {
                    "name": STRING,
                    "type": STRING,
                    "label": STRING,
                    "startIndex": INT,
                    "endIndex": INT,
                    "iri": STRING
                }
            ]
        }
    ]
}
```

### Example Output

Here is an example of an output from the endpoint `/entitymentions?article=test.txt`. For simplification, only a single file has been processed by the Entity Recognizer and Linker:

```JSON
{
    "fileName": "data_from_A/test.txt",
    "language": "en",
    "sentences": [
        {
            "sentence": "Hi my name is marc",
            "sentenceStartIndex": 0,
            "sentenceEndIndex": 47,
            "entityMentions": [
                {
                    "name": "marc",
                    "type": "Entity",
                    "label": "GPE",
                    "startIndex": 14,
                    "endIndex": 18,
                    "iri": "knox-kb01.srv.aau.dk/marc"
                }
            ]
        }
    ]
}
```


## /entitymentions/all <sup><span style="color:lightgreen">GET</span></sup>

The `/entitymentions/all` endpoint is a <span style="color:lightgreen">**GET**</span> endpoint. When doing a <span style="color:lightgreen">**GET**</span> request to the endpoint, a JSON Array is returned containing the all articles with their currently known entitymentions found. The JSON array is formatted as follows:

```JSON
[
    {
        "fileName": STRING,
        "language": STRING,
        "sentences": [
            {
                "sentence": STRING,
                "sentenceStartIndex": INT,
                "sentenceEndIndex": INT,
                "entityMentions": [
                    {
                        "name": STRING,
                        "type": STRING,
                        "label": STRING,
                        "startIndex": INT,
                        "endIndex": INT,
                        "iri": STRING
                    }
                ]
            }
        ]
    }
]
```

### Example Output

Here is an example of an output from the endpoint when getting all articles. For simplification, only two files has been processed by the Entity Recognizer and Linker:

```JSON
[
    {
        "fileName": "data_from_A/test.txt",
        "language": "en",
        "sentences": [
            {
                "sentence": "Hi my name is marc",
                "sentenceStartIndex": 0,
                "sentenceEndIndex": 47,
                "entityMentions": [
                    {
                        "name": "marc",
                        "type": "Entity",
                        "label": "PERSON",
                        "startIndex": 14,
                        "endIndex": 18,
                        "iri": "knox-kb01.srv.aau.dk/marc"
                    }
                ]
            }
        ]
    },
    {
        "fileName": "data_from_A/test2.txt",
        "language": "en",
        "sentences": [
            {
                "sentence": "Hi my name is joe",
                "sentenceStartIndex": 0,
                "sentenceEndIndex": 47,
                "entityMentions": [
                    {
                        "name": "Joe",
                        "type": "Entity",
                        "label": "PERSON",
                        "startIndex": 14,
                        "endIndex": 17,
                        "iri": "knox-kb01.srv.aau.dk/joe"
                    }
                ]
            }
        ]
    }
]
```



## /detectlanguage <sup><span style="color:orange">POST</span></sup>
This endpoint expects the given request body to contain some input text and returns its language. It uses the [langdetect](https://pypi.org/project/langdetect/) library.

> **_NOTE:_** The function will return the language as a [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code.

### Example
<span style="color:orange">Request body: </span> "The man was walking down the street"\
<span style="color:orange">Response: </span> en


### Constraints
- The given text has to be longer than 4 characters.

### Supported languages
`af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw`

> **_NOTE:_** see [List of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for more information