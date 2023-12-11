# Pipeline output
The pipeline output is a [JSON](https://en.wikipedia.org/wiki/JSON) structure containing the entitymentions and links for a given article

## The [JSON](https://en.wikipedia.org/wiki/JSON) output
```JSON
    {
        "fileName": STRING,
        "language": STRING,
        "metadataId": UUID (STRING),
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
                        "iri": STRING?
                    }
                ]
            }
        ]
    }
```
Here we see a file (article) contains a language (detected by the [Language Detector](https://pypi.org/project/langdetect/)), a metadataId (forwarded by **pipeline A**), as well as a list of sentences, further consisting of a list of entity mentions. 
> _**NOTE**_: The `iri` property can be null

## Example [JSON](https://en.wikipedia.org/wiki/JSON) output
```JSON
{
        "language": "en",
        "metadataId": "790261e8-b8ec-4801-9cbd-00263bcc666d",
        "sentences": [
            {
                "sentence": "Barrack Obama was married to Michelle Obama two days ago.",
                "sentenceStartIndex": 20,
                "sentenceEndIndex": 62,
                "entityMentions": 
                [
                    { "name": "Barrack Obama", "type": "Entity", "label": "PERSON", "startIndex": 0, "endIndex": 12, "iri": "knox-kb01.srv.aau.dk/Barack_Obama" },
                    { "name": "Michelle Obama", "type": "Entity", "label": "PERSON", "startIndex": 59, "endIndex": 73, "iri": "knox-kb01.srv.aau.dk/Michele_Obama" },
                    { "name": "two days ago", "type": "Literal", "label": "DATE",    "startIndex": 74, "endIndex": 86, "iri": null }
                ]
            }
        ]
    }
```

## Sending the [JSON](https://en.wikipedia.org/wiki/JSON) output to pipeline C
Lastly the [JSON](https://en.wikipedia.org/wiki/JSON) output is sent to **pipeline C** using a `POST` request. See [the code](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/e442dc496002b788d30f996cdfc87d36f5bcaa35/main.py#L32) for implementation details.

-----------
<div style="text-align: left">
    Go back to:
    <br>
    <span class="pagination_icon__3ocd0"><svg class="with-icon_icon__MHUeb" data-testid="geist-icon" fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24" style="color: currentcolor; width: 11px; height: 11px;"><path d="M15 18l-6-6 6-6"></path></svg></span>
    <a href="https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/entitylinker.md">Entity Linker</a>
    
</div>