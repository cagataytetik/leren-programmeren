naam = input("Wat is jou naam?: ")

ready = input("Ben je ready om een avontuur te beleven? (ja of nee)?: ")

if ready == "ja":
    vraag1 = input(f"Oke {naam} naar waar wil je toe A(Woestijn, B(Bergen, C(Bos: ")
else:
    print("Watje...")
    exit()


if vraag1 == 'a':
    vraag2 = input("je ziet water op de grond neem je het mee (ja of nee)")
    if vraag2 == "ja":
        vraag3 = input("je krijgt de keuze om 5 kilometer naar rechts te lopen of naar links wat kies je (links of rechts)")  
        if vraag3 == "links":
            print("je komt een vliegtuig tegen die je brengt naar huis Gefeliciteerd")
        elif vraag3 == "rechts":
            print("je ging dood door de warmte")
    if vraag2 == "nee":
        print("je gaat dood door de warmte")
    exit()
elif vraag1 == "b":
    vraag4 = input("Je klimt op de berg het begint steeds kouder te worden... Je ziet een een grot.. A(in de grot lopen? B(verder lopen?: ")
    if vraag4 == "a":
        print("Je werd door een beer opgegeten in de grot R.I.P.....")
        exit()
    else:
        vraag5 = input("Je liep verder en je kwam een huisje tegen wil je naar die huisje gaan? (ja of nee)?: ")
        if vraag5 == "ja":
            print("Je hebt een wizard in het huis gevonden hij teleporteerd je terug naar de bestemming... Gefeliciteerd!")
            exit()
        else:
            print("Waarom ging je niet naar het huisje? je friest nu dood... R.I.P")
else:
    vraag6 = input("Je loopt nu door de bos.. het word best donker... A(Vuurtje maken en ergens slapen B(Door lopen?")
    if vraag6 == "a":
       vraag7 = input("Je bent voor hout aan t zoeken je hoort rare geluiden ga je erop af? (ja of nee)?: ")
       if vraag7 == "ja":
            print("Je vind een portaal je stapt erin en hij brengt je thuis gefeliciteerd!!")
            exit() 

       else:
        print("Je gaat weer terug hout zoeken maar je valt in een trap... R.I.P")

    else:
        print("Je bent verdwaald geraakt in het bos je gaat dood van het honger R.I.P")