def bereken_poten(giraffe, struisvogel, zebra):
    zebrapoten = 4 * zebra
    giraffepoten = 4 * giraffe
    struisvogelpoten = 2 * struisvogel
    totale_poten = giraffepoten + struisvogelpoten + zebrapoten
    return totale_poten
print(bereken_poten(4, 2, 4))

#opdracht 2

tekst = """En ze stu[re]n [i]ngekleurde prentbriefkaarten van plekken waarvan ze zich niet reali[s]eren dat ze er nooit geweest zijn [a]an ' Iedereen op nummer 22, weer is prachti[g], onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[ ]i[s] vettig , maar we hebben een geweldig leuk restaurantje gevonden in de achterstraatjes waar ze Heine[ke]n hebben en kaas en uien chips en iemand die "Een beetje verliefd" speel[t] op een a[c]cordeon ' en je zit vier dagen vast op Schip[h]ol voor je vijfdaagse vliegvakantie met niks anders te eten dan uitgedroogde voorverpakte boterhammen..."""
tussen_haakjes = ''
binnen_haakjes = False
for character in tekst:
    if binnen_haakjes and character != ']':
        tussen_haakjes += character
    elif character == '[':
        binnen_haakjes = True
    elif character == ']':
        binnen_haakjes = False
    
print(tussen_haakjes)

