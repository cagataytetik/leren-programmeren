land1 = input("welke land speelt er?:")
land2 = input("welke land speelt er?:")
land3 = input("welke land speelt er?:")
print (f"deze landen zitten in groep a",land1, land2, land3)
wedstrijd1land1doelpunten = input("doelpunten in 1e wedstrijd voor de 1e land:")
wedstrijd2land1doelpunten = input("doelpunten in 2e wedstrijd voor de 1e land:")
wedstrijd1land2doelpunten = input("doelpunten in 1e wedstrijd voor de 2e land:")
wedstrijd2land2doelpunten = input("doelpunten in 2e wedstrijd voor de 2e land:")
wedstrijd1land3doelpunten = input("doelpunten in 1e wedstrijd voor de 3e land:")
wedstrijd2land3doelpunten = input("doelpunten in 2e wedstrijd voor de 3e land:")
uitslagland1land2 = wedstrijd1land1doelpunten , wedstrijd1land2doelpunten
print ("uitslag 1e wedstrijd", uitslagland1land2)
uitslagland2land3 = wedstrijd2land2doelpunten , wedstrijd1land3doelpunten
print ("uitslag 2e wedstrijd", uitslagland2land3)
uitslagland1land3 = wedstrijd2land1doelpunten , wedstrijd2land3doelpunten
print ("uitslag 3e wedstrijd", uitslagland1land3)