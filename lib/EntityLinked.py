from lib.Entity import Entity


class EntityLinked(Entity):
    def __init__(self, entity: Entity, iri: str):
        super().__init__(
            entity.name, entity.startIndex, entity.endIndex, entity.label, entity.type
        )
        self.iri = iri.replace(" ", "_")
