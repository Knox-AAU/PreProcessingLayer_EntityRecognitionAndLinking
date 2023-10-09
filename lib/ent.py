class Entity:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def serialize(self):
        return {
            "name": self.name,
            "index": self.index
        }
