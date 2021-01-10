t = int(input())
while t:
    t-=1
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    if k<=arr[0]:
        print(0)
    else:
        print(k-arr[0])