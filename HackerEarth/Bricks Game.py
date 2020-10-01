n=int(input())
c=[]
i=1
while sum(c)<n:
    a =i
    c.append(a)
    if sum(c)<=n:
        
        if (n-sum(c))<(i*2):
            c.append(n-sum(c))
        else:
            b = i*2
            c.append(b)
    i +=1

if(len(c)%2==0):
    print("Motu")
else:
    print("Patlu")
