from lib.Entity import Entity

class EntityLinked(Entity):
    def __init__(self, entity, linkId):
        super().__init__(entity.name, entity.startIndex, entity.endIndex, entity.fileName)
        self.linkId = linkId
