from components import *
import sys
def main():
    doc = GetSpacyData.GetTokens("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")
    ents = GetSpacyData.GetEntities(doc)  

    print(ents)
if __name__ == '__main__':
    sys.exit(main())
