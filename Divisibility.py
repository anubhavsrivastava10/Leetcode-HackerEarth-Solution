N = int(input())
data = [int(x) for x in input().split()]
D=[]
for x in data:
    lastdigit = (repr(x)[-1])
    D.append(lastdigit)
res = "".join(D)
res=int(res)
if(res%10==0):
    print("YES")
else:
    print("NO")
