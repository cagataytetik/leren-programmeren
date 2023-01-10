goed = False
while not goed:
    try:
        getal = int(input("Voer een getal in waarvan je de tafel wilt weten!:"))
        goed = True
    except:
        print("voer een getal in")


print (f"De tafel van {getal} is:")
for t in range(1,11):
    som = getal * t
    print (f"{t} x {getal} = {som}")
