import json


class Entity:
    def __init__(self, name, startIndex, endIndex, fileName):
        self.name = name
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.fileName = fileName
    
    #Not used - previously required appending, which was hard/unnecessary to implement
    def getEntity(self):
        return {
            
        }
