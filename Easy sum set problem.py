A=int(input())
lst1=list(map(int,input().split()))
B=int(input())
lst2=list(map(int,input().split()))
max1=max(max(lst1),max(lst2))
for i in range(max1):
    d=0
    for t in range(A):
        for u in range(B):
            if i+lst1[t] is lst2[u]:
                d=d+1
                break
    if d is A:
        print(i,'',end='')
