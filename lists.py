n=int(input("enter the no of commands: "))
list=[]
for a in range(n):
    b=(input(f"enter the command {a+1}: ").split())
    if b[0]=='insert':
        list.insert(int(b[1]),int(b[2]))
    elif b[0]=='print':
        print(list)
    elif b[0]=='remove':
        list.remove(int(b[1]))
    elif b[0]=='append':
        list.append(int(b[1]))
    elif b[0]=='sort':
        list.sort()
    elif b[0]=='pop':
        list.pop(int(b[1]))
    elif b[0]=='reverse':
        list.reverse()


# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reve