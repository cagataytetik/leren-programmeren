naam = input("Wat is jou naam?: ")
ready = input("Ben je ready om een avontuur te beleven? (ja of nee)?: ").lower()
lengte = int(input("wat is je lengte?:"))
if ready == "ja":
    vraag1 = input(f"Oke {naam} waar wil je naar toe A(Woestijn, B(Bergen, C(Bos: ").lower()
else:
    print("Watje...")



if vraag1 == 'a':
    vraag2 = input("je ziet water op de grond neem je het mee (ja of nee)").lower()
    if vraag2 == "ja":
        print("je hebt het opgepakt")
        vraag3 = input("je krijgt de keuze om 5 kilometer naar rechts te lopen of naar links wat kies je (links of rechts)").lower()
        if vraag3 == "links":
            print("je komt een vliegtuig tegen die je brengt naar huis Gefeliciteerd")
        elif vraag3 == "rechts":
            print("je werd gebeten door een reptiel door het gif sterf je... R.I.P")
    else:
        print("je droogt uit... R.I.P")
    
elif vraag1 == "b":
    vraag4 = input("Je klimt op de berg het begint steeds kouder te worden... Je ziet een een grot.. A(in de grot lopen? B(verder lopen?: ").lower()
    if vraag4 == "a" and lengte >= 180:
            print ("je past niet in de grot je gaat door bij de berg")
    if vraag4 == "a" and lengte <= 180:
        print("Je werd door een beer opgegeten in de grot R.I.P.....")
    else:
        vraag5 = input("Je liep verder en je kwam een huisje tegen wil je naar die huisje gaan? (ja of nee)?: ").lower()
        if vraag5 == "ja":
            print("Je hebt een wizard in het huis gevonden hij teleporteerd je terug naar de bestemming... Gefeliciteerd!")
        else:
            print("Waarom ging je niet naar het huisje? je friest nu dood... R.I.P")
else:
    vraag6 = input("Je loopt nu door de bos.. het word best donker... A(Vuurtje maken en ergens slapen B(Door lopen?").lower()
    if vraag6 == "a":
       vraag7 = input("Je bent voor hout aan t zoeken je hoort rare geluiden ga je erop af? (ja of nee)?: ").lower()
       if vraag7 == "ja":
            print("Je vind een portaal je stapt erin en hij brengt je thuis gefeliciteerd!!")
       else:
        print("Je gaat weer terug hout zoeken maar je valt in een trap... R.I.P")

    else:
        print("Je bent verdwaald geraakt in het bos je gaat dood van de honger R.I.P")