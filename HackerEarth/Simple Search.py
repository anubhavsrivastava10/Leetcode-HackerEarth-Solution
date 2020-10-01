N = int(input())
lst = list(map(int,input().split()))
X = int(input())
for i in range(0,len(lst)):
    if X == lst[i]:
        print(i)
