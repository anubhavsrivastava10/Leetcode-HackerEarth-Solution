c=0
for i in  range(0,int(input())):
    r,x= map(int,input().split())
    cir = 2*r*22/7
    if(cir<=100*x):
        c=c+1
print(c)
