x,y,p,q = map(int,input().split())

mul = y*p
carbon = int(mul/2)
value = min(carbon,q,y)

c1 = carbon/value
h1 = q/value
ch = y/value

if c1-int(c1)==0.0 and h1-int(h1)==0.0 and ch-int(ch)==0.0:
    carbon=c1
    q=h1
    y=ch

print(carbon,q,y)