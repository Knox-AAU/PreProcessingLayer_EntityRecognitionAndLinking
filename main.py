from components import *
import sys
from lib.ent import Entity
def main():
    doc = GetSpacyData.getspacydataFunc("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")
    
    ent = Entity(doc.ents[0].text, (doc.ents[0].start_char, doc.ents[0].end_char))
    print(ent.name)
    print(ent.index)
if __name__ == '__main__':
    sys.exit(main())
