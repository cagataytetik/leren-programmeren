def vraag_en_controleer_leeftijd(vraag: str) -> int:
    while True:
        leeftijd_string = input ("wat is je leeftijd")
        if not leeftijd_string.isnumeric():
            print("voer cijfers in!")
        elif int(leeftijd_string) < 0:
            print ("U moet nog geboren worden!")
        else:
            leeftijd = int(leeftijd_string)
            break
    return leeftijd




naam = input("hoe heet je?:")
age = vraag_en_controleer_leeftijd("Hoe oud ben je?:")
leeftijd_moeder = vraag_en_controleer_leeftijd("Hoe oud ben je?:")
print(f"Hallo {naam}, je leeftijd is: {age}")