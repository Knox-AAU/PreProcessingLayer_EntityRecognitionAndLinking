from components import *
import sys
from lib import Entity

def main():
    doc = GetSpacyData.getspacydataFunc("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")

    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

if __name__ == '__main__':
    sys.exit(main())