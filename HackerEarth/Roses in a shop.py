x = int(input())
lst = list(map(int,input().split()))[::-1]
count=0
ls=[]
for i in range(x):
    item = lst[i]
    for j in range(i,x):
        if lst[j]>item:
            count+=1
    ls.append(count)
    count=0
print(ls)