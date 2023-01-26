dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("alle dagen van de week zijn")

for s in dagen:
    print(s)

print("alle werkdagen zijn")

for o in dagen[0:5]:
    print(o)

print ("alle weekend dagen zijn")

for a in dagen[5:7]:
    print(a)

print ("alle dagen van de week omgedraaid zijn")

for d in reversed(dagen):
    print(d)

print ("alle weekend dagen van de week omgedraaid zijn")

for p in reversed(dagen[5:7]):
    print (p)

print ("alle werkdagen van de week omgedraaid zijn")

for q in reversed(dagen[0:5]):
    print(q)