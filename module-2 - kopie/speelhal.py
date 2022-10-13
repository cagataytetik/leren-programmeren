ticketkost = 7.45
vrienden = 4
prijs_vip = 0.37
permin = 5
Totalmin = 45

prijs = ticketkost * vrienden + Totalmin / permin * prijs_vip * vrienden

print ("Dagje uit met" ' '+ str(vrienden) +' ' "mensen in speelhal met" ' ' + str(Totalmin) + ' ' "minuten VR kost maar", prijs, "euro")