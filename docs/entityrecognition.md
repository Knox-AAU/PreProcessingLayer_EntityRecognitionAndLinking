# Entity Recognition

The entity recognition part is performed by using danish and english pre-trained models published by SpaCy.

## Model Links

- Danish model: [https://spacy.io/models/da#da_core_news_lg](https://spacy.io/models/da#da_core_news_lg)
- English model: [https://spacy.io/models/en#en_core_web_lg](https://spacy.io/models/en#en_core_web_lg)

## Custom Danish Model

The danish model has been trained on top of the danish pre-trained SpaCy model to improve its accuracy and be able to recognize literals. See [Pypi Repository](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/pypi.md) for more information on where to find the custom model.

## Loading a SpaCy Model

```python
import en_core_web_lg
import da_core_news_knox_lg

nlp_en = en_core_web_lg.load()
nlp_da = da_core_news_knox_lg.load()
```

> Full code available [here](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/5fcd59bac0fbd91b2543d7d78a893f16da49f25f/components/GetSpacyData.py#L17#L18).

## Performing Entity Recognition on Input

The entity recognition is performed using either the `nlp_en` or `nlp_da` variable defined in [Loading a SpaCy Model](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/entityrecognition.md#loading-a-spacy-model).

```python
def GetTokens(text: str):
    result = DetectLang(text)
    if result == "da":
        return nlp_da(text)
    elif result == "en":
        return nlp_en(text)
    else:
        raise UndetectedLanguageException()
```

> Full code available [here](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/5fcd59bac0fbd91b2543d7d78a893f16da49f25f/components/GetSpacyData.py#L31#L38).

The return type of this function is a [Doc](https://spacy.io/api/doc) containing information such as the entity's start and end index, the entity's belonging sentence, and so on.

---

<div style="text-align: right">
    Up next:
    <br>
    <a href="https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/entitylinker.md">Entity Linker</a>
    <span class="pagination_icon__3ocd0"><svg class="with-icon_icon__MHUeb" data-testid="geist-icon" fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24" style="color:currentColor;width:11px;height:11px"><path d="M9 18l6-6-6-6"></path></svg></span>
</div>
