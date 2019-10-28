x=input()
check = 0
l = ['A','E','I','O','U','Y']
if((int(x[0])+int(x[1]))%2==1):
    check = 1
if((int(x[3])+int(x[4]))%2==1):
    check = 1
if((int(x[4])+int(x[5]))%2==1):
    check = 1
if((int(x[7])+int(x[8]))%2==1):
    check = 1
if x[2] in l:
    check = 1
if(check==0):
    print('valid')
else:
    print('invalid')
