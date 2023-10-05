from components import *
import sys
import signal
def main():
    doc = GetSpacyData.GetTokens("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")
    ents = GetSpacyData.GetEntities(doc)  

    print(ents)
    signal.pause()
if __name__ == '__main__':
    sys.exit(main())
