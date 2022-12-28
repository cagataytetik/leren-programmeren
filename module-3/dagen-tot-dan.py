dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]


dag = int(input("Kies een dag van de week! (in cijfers) bv maandag = 1 dinsdag = 2 woensdag = 3 donderdag = 4 vrijdag = 5 zaterdag = 6 zondag = 7"))
k = 0
while k < dag:
    print(dagen[k])
    k = k + 1