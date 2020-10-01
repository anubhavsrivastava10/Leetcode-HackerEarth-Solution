a,b = map(int, input().split())
lst = [0] + list(map(int, input().split()))
for i in range(a):
    lst[i+1] += lst[i]
for i in range(b):
    x, y = map(int, input().split())
    print((lst[y]-lst[x-1])//(y-x+1))
