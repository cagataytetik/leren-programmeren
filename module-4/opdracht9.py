from fruitmand import fruitmand
newFruitmand = [
    item for item in fruitmand if item.get('name') != "druif"
]
kleur = [a['color'] for a in newFruitmand if 'color' in a]
lijst = []
for a in kleur:
    if a in lijst:
        continue
    print(a)
    lijst.append(a)