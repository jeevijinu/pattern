rows=int(input("enter value : "))
space=rows-1
for i in range(0,rows):
    for j in range(0,space):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    space=space-1
    print()
space=1
for i in range(rows-1,0,-1):
    for j in range(0,space):
        print(" ",end="")
    for k in range(0,i):
        print("* ",end="")
    space=space+1
    print()
