
print (" Solicitatieformulier Circusdirecteur voor Circus HotelDeBotel ")
print (" Er worden u een aantal vragen gesteld...                      ")
print (" Gelieve die naar eer en geweten in te vullen.                 ")
print (" Als u aan de criteria voldoet dan komt u in                   ")
print (" aanmerking voor een serieus sollicitatiegesprek!              ")
print (" hier komen de vragen.                                         ")



praktijk = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur?:"))
diploma = input ("Bent u in bezit van een Diploma MBO-4 ondernemen? ja/nee:")
naam = input ("Wat is uw naam?:")
rijbewijs = input ("Bent u in bezit van een geldig Vrachtwagen rijbewijs? ja/nee:")
hoed = input ("Bent u in bezit van een hoge hoed? ja/nee:")
manvrouw = input ("Bent u een vrouw of een man?:")

if manvrouw == "man":
    snor = input ("Heeft u een snor? ja/nee:")
    if snor == "ja":
        snorLengte = int(input("Hoelang is uw snor? (in cm):"))

elif manvrouw == "vrouw":
    krullen = input("Heeft u rood krullend haar? ja/nee:")
    if krullen == "ja":
        krullenlengte = int(input("Hoelang is uw rood krullend haar? (in cm):"))
    
    

certificaat = input ("Heeft u een overleven met een gevaarlijk persoon certificaat? ja/nee:")
veter = input ("Heeft u een Veterstrikdiploma? ja/nee:")
lengte = int(input ("Wat is uw lengte? (in cm):"))
gewicht = int(input ("Wat is uw gewicht? (in kg):"))
voorhoofd = input ("Heeft u een lange voorhoofd? ja/nee:")
kaas = input ("Heeft u ooit kaas gegeten? ja/nee:")

if praktijk > 4 and diploma == "ja" and rijbewijs == "ja" and hoed == "ja" and (manvrouw == "vrouw" and krullen == "ja" and  krullenlengte > 20) or (manvrouw == "man" and snor == "ja" and snorLengte > 10) and lengte > 150 and gewicht > 90 and certificaat == "ja" and veter == "ja" and voorhoofd == "ja" and kaas == "ja":
    print ("Gefeliciteerd! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV!")
else:
     print ("U voldoet niet aan onze eisen voor de functie van Circusdirecteur, het spijt ons!")