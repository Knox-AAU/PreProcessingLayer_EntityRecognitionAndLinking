class Entity:
    def __init__(self, name: str, startIndex: int, endIndex: int, sentence: str, sentenceStartIndex: int, sentenceEndIndex: int):
        self.name = name
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.sentence = sentence
        self.sentenceStartIndex = sentenceStartIndex
        self.sentenceEndIndex = sentenceEndIndex