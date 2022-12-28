from time import sleep
a = 30
delay = 0.2
print("De lancering gaat van start!")
while a > 0:
    print(a)
    a = a - 1
    sleep(delay)
print("De raket is gelanceerd!!")