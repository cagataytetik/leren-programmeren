import random
getal = 1
kleurenlijst = ['rood', 'blauw', 'groen', 'geel', 'bruin']
toevoegen = int(input("Hoeveel M&M's moeten er gevoegd worden:"))
BagOfMnMs = {}
for a in range(toevoegen):
    kleur = random.choice(kleurenlijst)
    if kleur not in BagOfMnMs:
        BagOfMnMs.update({kleur: getal})
    elif kleur in BagOfMnMs:
        BagOfMnMs[kleur] +=1
        print(BagOfMnMs)