N = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
counter = 0
x=0
if lst[0]<=0: #consider is all the values in the list are negative
    counter = max(lst)
    x=1
else:
    for i in lst:
        if i>=0:
            counter = counter + i
            x = x+1
print(counter,x)
