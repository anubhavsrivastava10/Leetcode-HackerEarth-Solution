n, m, g = map(int,input().split())
time = list(map(int,input().split()))
arr = list(map(int,input().split()))
lst = []
counter= 0
for i in range(0,n-1):
    x = time[i+1]-time[i]
    lst.append(x)
m = max(lst)
for j in range(0,m):
    if(m>=arr[j]):
        counter=counter+1
print(counter)
