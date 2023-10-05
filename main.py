from components import *
import sys
import time
def main():
    doc = GetSpacyData.GetTokens("Lars Løkke Rasmussen var statsminister i Danmark. Han er politiker for det Venstre orienterede parti.")
    ents = GetSpacyData.GetEntities(doc)
    let longtime = 0

    print(ents)
    while(longtime < 1000):
        time.sleep(5)
        longtime = longtime + 1
if __name__ == '__main__':
    sys.exit(main())
