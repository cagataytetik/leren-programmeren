import random
M_en_Ms = ("oranje", "blauw", "groen", "bruin","paars")
vraag = int(input("Hoeveel M&Ms er aan de zak toegevoegd worden?: "))
for u in range(vraag):
    print(random.choice(M_en_Ms))