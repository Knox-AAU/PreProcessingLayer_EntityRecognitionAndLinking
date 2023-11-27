class Entity:
    def __init__(self, name: str, startIndex: int, endIndex: int, label: str, type: str):
        self.name = name
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.label = label
        self.type = type