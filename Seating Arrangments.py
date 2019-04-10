x = int(input())
for i in range(0,x):
    n = int(input())
    t2=n
    t2-=1
    t1=int(t2/12)
    req=13+(t1*24)-n
    if((n%12)==1 or (n%12)==6 or (n%12)==7 or (n%12)==0):
        print(req,"WS")
    elif((n%12)==2 or (n%12)==5 or (n%12)==8 or (n%12)==11):
        print(req,"MS")
    elif((n%12)==3 or (n%12)==4 or (n%12)==9 or (n%12)==10):
        print(req,"AS")
