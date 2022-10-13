ticketkost = int(input("vul hier de prijs in centen in van de ticketkost:"))

vrienden = int(input("vul hier het aantal personen in:"))

prijs_vip = int(input("vul hier de prijs van vip in centen in:"))

permin = int(input("vul hier de vip minuten in:"))

Totalmin = int(input("vul hier de totale minuten in:"))

prijs = ticketkost / 100 * vrienden + Totalmin / permin * prijs_vip / 100 * vrienden

print ("dagje uit met" ' '+ str(vrienden) +' ' "mensen in de speelhal met" ' ' + str(Totalmin) + ' ' "minuten vr kost maar", prijs, "euro")