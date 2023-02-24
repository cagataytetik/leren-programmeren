from fruitmand import fruitmand
import random

aantal = int(input("Hoeveel fruit wilt u?: "))

fruiten = [b['name'] for b in fruitmand if 'name' in b]

fruit = (random.choices(fruiten, k=aantal))

for c in fruit:
    print(c)



