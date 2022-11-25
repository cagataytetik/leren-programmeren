import random

naam = input("hoe heet je?")
aantal_complimenten = int(input("hoevaak wil je het printen?"))

if aantal_complimenten == random.randint(1, 2) == 1:
    for x in range (aantal_complimenten):
        print (f"je bent geweldig {naam}")

elif aantal_complimenten == random.randint(1, 2) == 2:
    for x in range (aantal_complimenten):
     print (f"goed gedaan {naam}")

#variant 1 ==  lijsten
#variant 2 != lijsten randint(2, 4)

