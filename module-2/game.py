
naam = input("Wat is jou naam?: ")

ready = input("Ben je ready om een avontuur te beleven? (ja of nee)?: ").lower()

if ready == "ja":
    vraag1 = input(f"Oke {naam} naar waar wil je toe A(Woestijn, B(Bergen, C(Bos: ").lower()
else:
    print("Watje...")
    exit()

if vraag1 == 'a':
    print("Je ging zonder water naar de woestijn je sterfte uiteindelijk van de dorst....")
    exit()
elif vraag1 == "b":
    vraag2 = input("Je klimt op de berg het begint steeds kouder te worden... Je ziet een een grot.. A(in de grot lopen? B(verder lopen?: ").lower()
    if vraag2 == "a":
        print("Je werd door een beer opgegeten in de grot R.I.P.....")
        exit()
    else:
        vraag3 = input("Je liep verder en je kwam een huisje tegen wil je naar die huisje gaan? (ja of nee)?: ")
        if vraag3 == "ja":
            print("Je hebt een wizard in het huis gevonden hij teleporteerd je terug naar de bestemming... Gefeliciteerd!")
            exit()
        else:
            print("Waarom ging je niet naar het huisje? je friest nu dood... R.I.P")
else:
    vraag4 = input("Je loopt nu door de bos.. het word best donker... A(Vuurtje maken en ergens slapen B(Door lopen?").lower()
    if vraag4 == "a":
       vraag5 = input("Je bent voor hout aan t zoeken je hoort rare geluiden ga je erop af? (ja of nee)?: ").lower()
       if vraag5 == "ja":
            print("Je vind een portaal je stapt erin en hij brengt je thuis gefeliciteerd!!")
            exit()

       else:
        print("Je gaat weer terug hout zoeken maar je valt in een trap... R.I.P")

    else:
        print("Je bent verdwaald geraakt in het bos je gaat dood van het honger R.I.P")