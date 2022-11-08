print('Welcome to the football quiz')
answer=input('Are you ready to play the footbal Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: Wie is je favoriete voetbalspeler?')
if answer.lower()=='messi':
        score += 1
        print('correct')
else:
        print('Wrong Answer :(')
 
 
answer=input('Question 2: Wat is de beste voetbalclub? ')
if answer.lower()=='psg':
        score += 1
        print('correct')
else:
        print('Wrong Answer :(')
 
answer=input('Question 3: wie heeft de ballondor gewonnen?')
if answer.lower()=='benzema':
        score += 1
        print('correct')
else:
        print('Wrong Answer :(')
answer=input('Question 4: wie won de wk in 2020')
if answer.lower()=='italie':
        score += 1
        print('correct')
else:
        print('Wrong Answer')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*75
print('Marks obtained:',mark)
print('BYE!')
