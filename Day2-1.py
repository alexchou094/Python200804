import random

x = random.randint(1,10)

y = input("Please guess a number between 1 ~ 10 :")
y = int(y) 
if y<=0 or y>10:
    print("Not in range")
elif x==y :
    print("Nice guess")
else:
    print("Wrong number")
    print("The right number is :",x)
 