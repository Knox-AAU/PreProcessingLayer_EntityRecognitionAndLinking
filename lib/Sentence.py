class Sentence:
    def __init__(self, fileName: str, text: str, startIndex: int, endIndex: int):
        self.fileName = fileName
        self.text = text
        self.startIndex = startIndex
        self.endIndex = endIndex