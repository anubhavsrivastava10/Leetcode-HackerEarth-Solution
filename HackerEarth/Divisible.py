N = int(input())
data = [int(x) for x in input().split()]
D=[]
y=int(N/2)
for x in data[0:y]:
    lastdigit = (repr(x)[0])
    D.append(lastdigit)
for x in data[y:]:
    lastdigit= repr(x)[-1]
    D.append(lastdigit)
res = "".join(D)
res=int(res)
if(res%11==0):
    print("OUI")
else:
    print("NON")
