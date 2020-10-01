# consider both cases w/b and b/w as it says compare sides

d = 0
for i in range(0,int(input())):
    w,b = map(int,input().split())
    c = w/b
    x = b/w
    if 1.6<=c<=1.7 or 1.6<=x<=1.7:
        d+=1
print(d)
