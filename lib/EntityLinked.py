from lib.Entity import Entity


class EntityLinked(Entity):
    def __init__(self, entity: Entity, iri: str):
        super().__init__(
            entity.name, entity.startIndex, entity.endIndex, entity.label, entity.type,entity.sentence, entity.sentenceStartIndex, entity.sentenceEndIndex
        )
        self.iri = iri.replace(" ", "_")

    def getEntityJSON(self):
        return {
            "name": self.name,
            "type": self.type,
            "label": self.label,
            "type": self.type,
            "startIndex": self.startIndex,
            "endIndex": self.endIndex,
            "iri": ("knox-kb01.srv.aau.dk/" + self.iri) if self.type == "Entity" else None
        }
