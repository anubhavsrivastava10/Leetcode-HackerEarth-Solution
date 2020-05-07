import itertools 
  
def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 

x = int(input())
lst = list(map(int,input().split()))
c=0
ls = []
for i in range(1,x+1):
    x = findsubsets(lst, i)
    print(x)
    for item in x:
        item = list(item)
        y = sum(item)
        if y%2==0:
            ls.append(y)
ls = set(ls)
print(len(ls))
