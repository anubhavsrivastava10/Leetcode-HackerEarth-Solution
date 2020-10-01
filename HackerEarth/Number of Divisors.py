for i in range(int(input())):
    n,k = map(int,input().split())
    su1 = n*(n+1)//2
    num = n//k
    for j in range(1,num+1):
        z = k*j
        su1-=z
        while(z%k==0):
            z = z//k
        su1+=z
    print(su1)