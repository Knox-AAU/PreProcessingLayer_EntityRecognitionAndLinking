from lib.Entity import Entity

class EntityLinked(Entity):
    def __init__(self, entity, iri):
        super().__init__(entity.name, entity.startIndex, entity.endIndex, entity.fileName)
        self.iri = iri.replace(" ", "_")
