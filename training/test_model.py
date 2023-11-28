import spacy

# Load your trained model
nlp = spacy.load("trainedmodel/updated_da_model")

# Evaluation data
eval_data = [
    (
        "I 1976 blev Apple opfundet",
        {"entities": [(0, 6, "LITERAL"), (12, 17, "ORG")]},
    ),
    (
        "iPhone 12 blev udgivet i 2020",
        {"entities": [(0, 9, "MISC"), (23, 29, "LITERAL")]},
    ),
    (
        "Det koster 1000 kr. at købe denne ting.",
        {"entities": [(11, 19, "LITERAL")]},
    ),
    (
        "I morgen skal jeg i skole.",
        {
            "entities": [
                (0, 8, "LITERAL"),
            ]
        },
    ),
    (
        "I dag skulle vi møde kl. 08:15.",
        {"entities": [(0, 5, "LITERAL"), (21, 30, "LITERAL")]},
    ),
    (
        "Vi skal aflevere d. 21/12/2023.",
        {"entities": [(17, 30, "LITERAL")]},
    ),
    (
        "Vestjyllands finansminister Jørgen Kofoed og hans børn, blev mandag d. 3. December opkøbt af storkoncernen Apple for 20 kr.",
        {
            "entities": [
                (0, 12, "LOCATION"),
                (28, 41, "PERSON"),
                (45, 54, "PERSON"),
                (61, 82, "LITERAL"),
                (107, 112, "ORG"),
                (117, 123, "LITERAL"),
            ]
        },
    ),
    (
        "George Bush var skyld i 9/11, og jeg skal til Struer d. 28/11/2023.",
        {
            "entities": [
                (0, 11, "PERSON"),
                (24, 28, "LITERAL"),
                (46, 52, "LOCATION"),
                (53, 66, "LITERAL"),
            ]
        },
    ),
    (
        "Peter gik over vejen og købte mælk og Epstein dræbte ikke sig selv for 2 dage siden.",
        {
            "entities": [
                (0, 5, "PERSON"),
                (38, 45, "PERSON"),
                (67, 83, "LITERAL"),
            ]
        },
    ),
]

# Initialize evaluation metrics
eval_metrics = {
    "correct": 0,
    "incorrect": 0,
    "missed": 0,
    "partial": 0,
    "spurious": 0,
}

# Evaluate the model
for text, annotations in eval_data:
    gold_entities = [
        text[start:end] for start, end, _ in annotations.get("entities", [])
    ]
    gold_labels = [
        label for start, end, label in annotations.get("entities", [])
    ]
    doc = nlp(text)

    print(f"Text: {text}")
    print("Gold Entities:", gold_entities)
    print("Gold Labels", gold_labels)

    recognized_entities = [ent.text for ent in doc.ents]
    recognized_labels = [ent.label_ for ent in doc.ents]
    print("Recognized Entities:", recognized_entities)
    print("Recognized Labels", recognized_labels)

    for ent in doc.ents:
        if ent.text in gold_entities:
            eval_metrics["correct"] += 1
        else:
            eval_metrics["spurious"] += 1

    for gold_entity in gold_entities:
        if gold_entity not in recognized_entities:
            eval_metrics["missed"] += 1
    print("\n---\n")
    if recognized_entities == gold_entities:
        print("PASSED")
    else:
        print("FAILED")
    print("\n---\n")

# Calculate precision, recall, and F1 score
precision = eval_metrics["correct"] / (
    eval_metrics["correct"] + eval_metrics["spurious"] + 1e-8
)
recall = eval_metrics["correct"] / (
    eval_metrics["correct"] + eval_metrics["missed"] + 1e-8
)
f1_score = 2 * (precision * recall) / (precision + recall + 1e-8)

print(
    f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1_score:.2f}"
)
