automerken = ("Opel" , "Merrie" , "volvie" , "rsq8")
kleuren = ("rood" , "blauw" , "grijs" , "geel" , "groen")
brochure = []
for merk in automerken:
    for kleur in kleuren:
        auto_in_kleuren = merk + " in " + kleur
        brochure.append(auto_in_kleuren)

print (brochure)