import os
import da_core_news_lg
import random
from spacy.training.example import Example
import shutil
from training_data import training_data
import time

starttime = time.time()
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

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time_seconds = end_time - starttime

# Convert seconds to days, hours, minutes, and seconds
days, remainder = divmod(elapsed_time_seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

# Print the training time
if days >= 1:
    print(
        f"Training finished in {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds!"
    )
elif hours >= 1:
    print(
        f"Training finished in {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds!"
    )
else:
    print(
        f"Training finished in {int(minutes)} minutes and {int(seconds)} seconds!"
    )

nlp.to_disk("trainedmodel/updated_da_model")
