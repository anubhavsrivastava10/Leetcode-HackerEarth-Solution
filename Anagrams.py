n=int(input())
for j in range(n):
    s1=list(input())
    s2=list(input())
    d=0
    m=len(s1)+len(s2)
    l1=set(s1).intersection(set(s2))
    for i in l1:
        d=d+min(s1.count(i),s2.count(i))
    print(m-2*d)
