import random
getal = 1
kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
mms = int(input("Hoeveel M&M's moeten er gevoegd worden: "))
zak = {}
for a in range(mms):
    kleur = random.choice(kleuren)
    if kleur not in zak:   
        zak.update({kleur: getal})
    elif kleur in zak:  
        zak[kleur] += 1

print(zak) 
