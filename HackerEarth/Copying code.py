n,i = map(int,input().split())
if n==i:
    print(0)
else:
    first = 4
    first += (n-i)
    second = (n-i)*2
    print(min(first,second))