# #feestlunch

crosaintjes = 17
prijsproduct = 0.39
stokbroden = 2
prijsproduct1 = 2.78
kortingsbonnen = 3
kortingsprijs = 0.50

prijs = (crosaintjes * prijsproduct + stokbroden * prijsproduct1 - kortingsbonnen * kortingsprijs)

print ("de feestlunch kost", prijs, "euro voor de" ' ',crosaintjes, ' ' "crosaintjes en de" ' ',stokbroden, ' ' "stokbroden als de" ' ',kortingsbonnen, ' ' " kortingsbonnen nog geldig zijn!")



#speelhal

vrienden = 4
prijs_vip = 0.37
permin = 5
Totalmin = 45

prijs =   vrienden * prijs_vip * 9

print ("Dagje uit met" ' '+ str(vrienden) +' ' "mensen in speelhal met" ' ' + str(Totalmin) +' ' "minuten VR kost maar", prijs, "euro")









tekst1 = "hallo wereld"
tekst2 = input("wat is je naam?")

print (f"{tekst1} ik ben {tekst2}")
print (tekst1 +' ik ben '+ tekst2)
print (tekst1, "ik ben" ,tekst2)