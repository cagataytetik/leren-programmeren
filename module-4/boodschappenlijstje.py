bag = {}
while True:
    vraag = input("Wil je een product toevoegen?: ").lower()
    if vraag == "nee":
        break
    product = input("Welke product wil je?: ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?: "))
    if product not in bag:
        bag.update({product: aantal})      
    else:
        bag[product] += aantal
print("-[ BOODSCHAPPENLIJST ]-")
for product, aantal in bag.items():
    print(f"{product} x {aantal}")
print("-----------------------")