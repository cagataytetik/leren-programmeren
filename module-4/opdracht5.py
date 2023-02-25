from fruitmand import fruitmand
fruiten = [a['name'] for a in fruitmand if 'name' in a]

for b in reversed(fruiten):
    print(b)