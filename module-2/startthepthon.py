gastheer = input("Wie is de gastheer")
gasten = 6
drank = True
chips = False

#een feest met chips, maar zonder drank kan niet beginnen
#een feest met gasten kan niet beginnen als er geen chips
#                                        en geen drank is





aanwezigen = gasten if gastheer == '' else gasten + 1
if drank and gastheer != 'rudi' and (gastheer or gasten >=5) and aanwezigen <= 13:
    print('Start the party')
else:
    gastheer == "Rudi"
    print('no party')