import json
class Entity:
    def __init__(self, name, startIndex, endIndex, fileName):
        self.name = name
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.fileName = fileName
    
    def getEntity(self):
        return {"name": self.name, "startIndex": self.startIndex, "endIndex": self.endIndex, "fileName": self.fileName}