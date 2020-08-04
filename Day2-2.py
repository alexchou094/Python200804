import random

x = random.randint(1,20)

while True:
    y = input("Guess a number : ")
    y = int(y)
    if y<1 or y>20:
       print("Not in range")
    else:
      if y>x:
          print("smaller")
      elif y<x:
          print("bigger")
      else:
          print("nice guess")
          break