d={}
item=None
val=None
i=int(input("enter the number of items: "))
for a in range(i):
    item=input(f"enter item {a+1}: ")
    val=input(f"enter value of {item}: ")
    # d.update({item : val})
    d[item]=val
print(d)
print(d[1])