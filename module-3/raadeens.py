import random
aantalBeurten = 0
score = 0
ronde_teller = 0
ronde_limiet = 20

print('Wat is je naam?')
mijnNaam = input()
while True:
    raden = input("Wil je een getal raden (ja of nee)?")
    if raden == "nee":
        break
    elif ronde_teller == ronde_limiet:
        break
    elif raden == "ja":
        getal = random.randint(1, 1000)
    print('OK ' + mijnNaam + ', ik denk aan een getal tussen 1 en 1000.')
    while aantalBeurten < 10:
        print('Raad eens.')
        poging = input()
        poging = int(poging)
        aantalBeurten = aantalBeurten + 1
        if poging < getal:
            print('Je hebt te laag geraden.')
        elif poging > getal:
            print('Je hebt te hoog geraden.') 
        verschil = abs (poging - getal)
        if verschil <=20:
            print ("maar je bent heel warm")
        elif verschil <=50:
            print ("maar je bent warm")
        if poging == getal:
            break
    if poging == getal:
        score = score + 1
        aantalBeurten = str(aantalBeurten)
        print('Goedzo, ' + mijnNaam + '! Je hebt het getal geraden in ' + aantalBeurten + ' beurten!')
        print ("Je huidige score is", score)
    elif poging != getal:
        getal = str(getal)
        print('Jammer. Het getal waar ik aan dacht was ' ,getal , '.')

    doorgaan = input("Wil je doorgaan (ja of nee)?")
    aantalBeurten = 0

    if doorgaan == "ja":
        ronde_teller = ronde_teller + 1
        print ('Je huidige score is ' , score , ' in ronde ' , ronde_teller)

    elif doorgaan == "nee":
        ronde_teller = ronde_teller + 1
        print ('Totziens. Je huidige score is ' ,score , ' in ronde ' , ronde_teller )