x = input()
sum1 = 0
j = 1
z = 0
y = str(x)
if len(y)!=10 :
    print('Illegal ISBN')
else:
    for i in x:
        i=int(i)
        sum1 = i * j
        j+=1
        z = z+sum1
    if z%11==0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
        
