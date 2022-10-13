iphone = int(input("hoe duur is de Iphone 13?"))
Galaxy = int(input("en hoe duur is de Samsung Galaxy S22?"))
verschil = iphone - Galaxy
verschil2 = Galaxy - iphone

if Galaxy > iphone:
    print(f" De galaxy is het duurst, de telefoon kost: {Galaxy} Euro")
    print(f" De iphone is het goedkoopst, de telefoon kost: {iphone} Euro")
    print(f" Het advies is dus de iphone te kopen, Deze is namelijk {verschil2} euro goedkoper dan de Galaxy")
elif Galaxy < iphone:
    print(f" De iphone is het duurst, de telefoon kost: {iphone} Euro")
    print(f" De Galaxy is het goedkoopst, de telefoon kost: {Galaxy} Euro")
    print(f" Het advies is dus de Galaxy te kopen, Deze is namelijk {verschil} euro goedkoper dan de iphone")
elif iphone <= Galaxy:
    print(f" Koop dan de iphone want deze kost evenduur als de Galaxy")