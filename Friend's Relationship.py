n=int(input())
for i in range(n):
    y=int(input())
    x=y*2
    for j in range(y):
        for k in range(x):
            if k>=j+1 and k<x-j-1:
                print("#",end="")
            else:
                print("*",end="")
        print()
