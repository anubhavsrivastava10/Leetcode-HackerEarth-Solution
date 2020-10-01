n,m = map(int,input().split())
lst = list(map(int,input().split()))
ls = list(map(int,input().split()))
lst = sorted(lst)[::-1]
ls = sorted(ls)[::-1]
if lst[0]>ls[0]:
    print(-1)
else:
    c=0
    k=1
    for _ in range(n//m):
        for i in range(m):
            if lst[i]<=ls[i]:
                c+=k
        k=2
    l = n%m
    l=l*2
    c+l
    print(c)