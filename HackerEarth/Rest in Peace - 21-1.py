n = int(input())
for i in range(0,n):
    x = int(input())
    if x%21==0:
        print('The streak is broken!')
    elif '21' in str(x):
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')
            
