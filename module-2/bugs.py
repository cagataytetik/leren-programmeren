import random

naam = input('Wat is jouw naam?')
print('Hallo', naam)

favorieteseizoen = input(f"Wat is jouw favorite seizoen {naam}? A) Lente, B) Zomer, C) Herfst of D) Winter?:")
antwoord = favorieteseizoen

if antwoord == "a":
    print("Ik hou ook van de lente!")
elif antwoord == "b":
    print("De zomer is voor mij te warm.")
elif antwoord == "c":
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif antwoord == "d":
    print("Is de winter niet erg koud?")
else:

    print("Die ken ik niet...")


favorietekleur = input('En wat is je favoriete kleur? ')

trueOrFalse = str(random.randint(0, 1))


if trueOrFalse:

    print('Ik vind dat ook een mooie kleur!')


elif not trueOrFalse:

    print('TBH, ik hou niet zo van'(favorietekleur))


num1 = random.randint(1, 10)

num2 = random.randint(5, 15)


try:

    number = int(input(f'En weet jij wat {num1} + {num2} is? '))

    if num1 + num2 == number:

        print('Dat is juist')

    else:

        print('Nee dat klopt niet'(naam))

except:

    print('Dat is geen nummer!')