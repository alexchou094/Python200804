import random
x = random.randint(1,20)
i = 0
while i<5:
    y = input("Guess a number : ")
    y = int(y)
    i=i+1
    if y<1 or y>20:
       print("Not in range")
    else:
      if y>x:
          print("smaller")
      elif y<x:
          print("bigger")
      else:
          print("nice guess")
          print('you have played ',i,'times')
          break