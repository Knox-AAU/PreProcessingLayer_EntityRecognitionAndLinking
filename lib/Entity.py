class Entity:
    def __init__(self, name: str, startIndex: int, endIndex: int, sentence: str, sentenceStartIndex: int, sentenceEndIndex: int, label: str, type: str):
        self.name = name
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.sentence = sentence
        self.sentenceStartIndex = sentenceStartIndex
        self.sentenceEndIndex = sentenceEndIndex
        self.label = label
        self.type = type