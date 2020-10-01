x = input()
a=0
b=0
for i in x:
    if i == 'L':
        a-=1
    elif i == 'R':
        a+=1
    elif i == 'U':
        b+=1
    elif i == 'D':
        b-=1
print(a,b)
