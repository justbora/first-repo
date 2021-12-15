n=int(input("enter the number of students: "))
amarks=[]
top=[]
for a in range(n):
    name=input(f"Enter thr name of {a+1} student: ")
    scores=(input(f"Enter the marks of {name}: ").split(','))
    score=list(scores)
    marks=list(map(float,scores))
    avg=sum(marks)/len(marks)
    amarks.append([name,avg])
    top.append(avg)

queryname=input("Enter name of student for average: ")
for val in amarks:
    if queryname==val[0]:
        print(f"The average marks of {queryname} is :{val[1]}")

for val in amarks:
    if max(top)==val[1]:
        print(f"Name of topper is: {val[0]}")