x, y, s, t = map(int,input().split())
counter = 0
for i in range(x,x+s+1):
    for j in range(y,y+s+1):
        if(i+j)<=t:
            counter = counter+1
print(counter)
