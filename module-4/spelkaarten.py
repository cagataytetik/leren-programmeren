import random
soorten = ["harten", "klaver", "schoppen", "ruiten"]
anderen = ["aas","boer", "vrouw", "heer"]
deck = ["joker", "joker2"]
for a in soorten:
    for b in anderen:
        deck.append(f"{a} {b}")
    for c in range(2,10,1):
        deck.append(f"{a} {c}")
random.shuffle(deck)
for d in range(1,8):
    kaart = random.choice(deck)
    print(f"kaart {d}: {kaart}")
    deck.remove(kaart)
print(f"deck (47 kaarten): {deck}")