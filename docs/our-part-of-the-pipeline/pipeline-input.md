# Pipeline input
The pipeline starts when a new file (article) is detected in a watched directory by the [DirectoryWatcher](https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/lib/DirectoryWatcher.py). This new file is produced by **pipeline A**

## Example input data
```txt
Since the sudden exit of the controversial CEO Martin Kjær last week, 
both he and the executive board in Region North Jutland 

have been in hiding. 
```
> some/article.txt

## Preprocessing the input
Before the Entity Recognizer can use the input, it must be preprocessed. This entails removing newlines and adding punctuation where needed.

### Example preprocessed input data
```txt
Since the sudden exit of the controversial CEO Martin Kjær last week, 
both he and the executive board in Region North Jutland.  have been in hiding.
```

-----------
<div style="text-align: right">
    Up next:
    <br>
    <a href="https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking/blob/main/docs/entityrecognition.md">Entity Recognition</a>
    <span class="pagination_icon__3ocd0"><svg class="with-icon_icon__MHUeb" data-testid="geist-icon" fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24" style="color:currentColor;width:11px;height:11px"><path d="M9 18l6-6-6-6"></path></svg></span>
</div>