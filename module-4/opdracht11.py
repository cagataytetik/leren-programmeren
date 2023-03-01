from fruitmand import fruitmand
ROND = 0
NIET_ROND = 0
beschikbaar_kleuren = [fruit["color"] for fruit in fruitmand]
while True:
    vraag = input("kies een kleur uit deze kleuren,(yellow)(brown)(red)(orange)(green): ")
    if vraag not in beschikbaar_kleuren:
        print(f"De kleur {vraag} zit er niet in de fruitmand")
        continue
    for fruit in fruitmand:
        if fruit["color"] == vraag:
            if fruit["round"] == True:
                ROND +=1
            else:
                NIET_ROND +=1
    if ROND > NIET_ROND:
        print(f"Er zijn {ROND-NIET_ROND} meer ROND vruchten dan niet ROND vruchten in de kleur {vraag}")
    elif ROND < NIET_ROND:
        print(f"Er zijn {NIET_ROND-ROND} minder ROND vruchten dan niet ROND vruchten in de kleur {vraag}")
    else:
        print(f"Er zijn {ROND} ROND vruchten en {NIET_ROND} niet ROND vruchten in de kleur {vraag}")    