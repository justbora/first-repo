n = int(input('Enter no. of students: '))
studentmarks={}
for a in range(n):
    name=input(f"Enter the name of {a+1} student: ")
    scores=input(f"Enter the marks of {name}: ").split(',')
    marks=list(map(float,scores))
    studentmarks.update({name : marks})
query_name = input("Enter name of student to get average marks: ")
a=studentmarks.get(query_name)
print(f"{sum(a)/len(a)}")
        