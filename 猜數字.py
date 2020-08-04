print("Please pick a number between 1~31 and remember it.")
Z = input("Ready ? type something continue : ")
A = ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29','31']
B = ['2','3','6','7','10','11','14','15','18','19','22','23','26','27','30','31']
C = ['4','5','6','7','12','13','14','15','20','21','22','23','28','29','30','31']
D = ['8','9','10','11','12','13','14','15','24','25','26','27','28','29','30','31']
E = ['16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
I = 1
while I == 1 :
    print("list A ",A)
    a = input('Is the list A has the number your pick ? if yes enter "1" ,if not enter "2" : ')
    a = int(a)
    if a != 1 and a != 2:
        print("wrong type!")
    else:
        print("list B ",B)
        b = input('Is the list B has the number your pick ? if yes enter "1" ,if not enter "2" : ')
        b = int(b)
        if b != 1 and b != 2:
            print("wrong type!")
        else:
            print("list C ",C)
            c = input('Is the list C has the number your pick ? if yes enter "1" ,if not enter "2" : ')
            c = int(c)
            if c != 1 and c != 2:
                print("wrong type!")
            else:
                print("list D ",D)
                d = input('Is the list D has the number your pick ? if yes enter "1" ,if not enter "2" : ')
                d = int(d)
                if d != 1 and d!= 2:
                    print("wrong type!")
                else:
                    print("list E ",E)
                    e = input('Is the list E has the number your pick ? if yes enter "1" ,if not enter "2" : ')
                    e = int(e)
                    if e !=1 and e != 2:
                        print("wrong type!")
                    else:
                        I = 0
x = 0
if a==1 :
    x=x+1
else:
    x=x+0
if b==1 :
    x=x+2
else:
    x=x+0
if c==1 :
    x=x+4
else:
    x=x+0
if d==1 :
    x=x+8
else:
    x=x+0
if e==1:
    x=x+16
else:
    x=x+0
print("I guess your number is :",x)

    

                       