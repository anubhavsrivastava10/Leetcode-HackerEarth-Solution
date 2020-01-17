K=int(input())
dict1={}
lst=list(map(int,input().split()))
k=int(input())
lst1=[]
for i in lst:
    dict1[i]=dict1.get(i,0)+1
for i,j in dict1.items():
    if j==k:
        lst1.append(i)
print(min(lst1))
