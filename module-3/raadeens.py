import random
AantalRondes = 20
KansenOmTeRaden = 10
kansen = 0
punten = 0
rondes = 0

while rondes < AantalRondes:
    raden = input("Wil je een getal raden? :").lower()
    if raden == "nee":
        print(f'je hebt {punten} punten in {AantalRondes} rondes')
        exit()

nummer = random.randint (1,1000)
print (nummer)