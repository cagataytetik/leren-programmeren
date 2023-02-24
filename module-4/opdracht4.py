from fruitmand import fruitmand
import random

aantal = int(input("Hoeveel fruit wilt u?: "))

fruiten = [a['name'] for a in fruitmand if 'name' in a]

fruit = (random.choices(fruiten, k=aantal))

for b in fruit:
    print(b)



