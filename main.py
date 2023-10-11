from components import *
import sys
import time
def main():
    text = GetSpacyData.GetText("Artikel.txt") #Takes in title of article. Gets article text in string format
    doc = GetSpacyData.GetTokens(text) #finds entities in text, returns entities in doc object
    ents = GetSpacyData.GetEntities(doc, "Artikel.txt") #appends entities in list
    entMentions= GetSpacyData.entityMentionJson(ents)  #Returns JSON object containing an array of entity mentions
    longtime = 0

    print(entMentions)
    
    while(longtime < 1000):
        time.sleep(5)
        longtime = longtime + 1
if __name__ == '__main__':
    sys.exit(main())
