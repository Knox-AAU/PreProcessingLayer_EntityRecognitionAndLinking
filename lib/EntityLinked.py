import Entity


class EntityLinked(Entity):
    def __init__(self, name, startIndex, endIndex, fileName, linkId):
        super().__init__(name, startIndex, endIndex, fileName)
        self.linkId = linkId
