import random
dag_stoppen = input("voer dag in waarop je wilt stoppen:")

for dag in ("ma", "di", "wo", "do", "vr", "za", "zo"):
    print (dag)
    if dag == dag_stoppen:
        break