print (f" cagatay Tetik pizza calculator:")


Prijs_small = 5
Prijs_medium = 8
Prijs_large = 11

small = int(input("hoeveel small pizzas wilt u?"))
medium = int(input("hoeveel medium pizzas wilt u?"))
large = int(input("hoeveel large pizzas wilt u?"))
if small >3:
  raise Exception ("je eet wel veel")

prijstotaal = small * Prijs_small + medium * Prijs_medium + large * Prijs_large

print (f"u heeft {small} small pizzas gekocht")
print (f"u heeft {medium} medium pizzas gekocht")
print (f"u heeft {large} large pizzas gekocht")

print (f" de totale prijs van de pizzas is {prijstotaal} euro")

print (f"bedankt dat u bij ons heeft besteld fijne dag")