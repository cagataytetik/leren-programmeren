from fruitmand import fruitmand
lengte = 0
langste_fruitnaam = {}
kleuren_dict = {"yellow" : "geel" ,"green":"groen","orange":"oranje","red":"rood","brown":"bruin",}
for fruit in fruitmand:
    if len(fruit["name"]) > lengte:
        lengte = len(fruit["name"])
        langste_fruitnaam = fruit
print(f"De",langste_fruitnaam['name'],(lengte),"heeft een",kleuren_dict[langste_fruitnaam['color']],"kleur","en een","gewicht","van",langste_fruitnaam["weight"]/1000,"kg.")