nP = input("how many student in your class?")
nP = int(nP)
total = 0
avg = 0
name = []
grade = []
for i in range(nP):
    N = input("Please enter students' name : ")
    name.append(N)
    G = input("Please enter the student's grade : ")
    grade.append(G)
for i in range(nP):
    total = total + int(grade[i])
print("The total grade is : ",total)
avg = total / nP
print("The average value is : ",avg)
H = 0
Hp = 0
for i in range(nP):
    if int(grade[i]) > H:
        H = int(grade[i])
        Hp = str(name[i])
print("The highest grade is",Hp,' : ',H,"point")
L = 0
Lp = 0
for i in range(nP):
    if int(grade[i]) < L:
        L = int(grade[i])
        Lp = str(name[i])
print("The lowest grade is",Lp,' : ',L,"point")
 
        
