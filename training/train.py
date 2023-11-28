import os
import spacy
import da_core_news_lg
import random
from spacy.training.example import Example
import shutil
from training_data import training_data

# Evaluate the model's predictions
if os.path.exists("trainedmodel/updated_da_model"):
    shutil.rmtree("trainedmodel")

if not os.path.exists("trainedmodel/updated_da_model"):
    os.makedirs("trainedmodel/updated_da_model")
# Load your pre-trained model
nlp = da_core_news_lg.load()

epochs = 22
dropout_rate = 0.35

gold_standard = [
    (
        "I 1976 blev Apple opfundet",
        {"entities": [(2, 6, "LITERAL"), (12, 17, "ORG")]},
    ),
    ("iPhone 12 blev udgivet i 2020", {"entities": [(25, 29, "LITERAL")]}),
]

if "ner" not in nlp.pipe_names:
    nlp.add_pipe("ner")

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]


for epoch in range(epochs):
    random.shuffle(training_data)
    losses = {}
    for text, annotations in training_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=dropout_rate, losses=losses)
    print(f"Ended Epoch {epoch} with loss: {losses['ner']}")


with nlp.disable_pipes(
    *other_pipes
):  # temporarily disable other pipelines during evaluation
    for text, annotations in gold_standard:
        doc = nlp(text)

nlp.to_disk("trainedmodel/updated_da_model")
