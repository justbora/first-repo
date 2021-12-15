res=[]
ms=[]
nam=[]
for a in range(int(input('enter no. of students: '))):
    name = input(f"enter name of {a+1} student: ")
    score = float(input(f'enter marks of {name}: '))
    res.append([name,score])
    ms.append(score)
print(res)
print(ms)    
ms=sorted(set(ms))
print(ms)
sl=ms[1]
for val in res:
    if sl==val[1]:
        nam.append(val[0])
nam.sort()
print(str(nam))