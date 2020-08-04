x = input("Please enter a number : ")
x = int(x)
M = 0 #是否為質數  1=是
T = 1 #計算用while 開關 0=關 1=開
i = 2 #計算用變數
while True :
    if x<=1:
        print("It isn't a prime number !")
        break
    else:
        while T == 1:
            if x == i:
                M =1
                break
            else:
                if x % i == 0:
                    T = 0
                else:
                    i=i+1
        if i == x and M == 1 :
            print("It's a prime number! ")
            break
        else :
            print("It isn't a prime number. ")
            break

   
       
       
        

