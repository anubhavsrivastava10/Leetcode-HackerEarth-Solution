A=0
B=7
for i in range(0,int(input())):
    floor = int(input())
    if(abs(floor-A)<=abs(B-floor)):
        print('A')
        A=floor
    else:
        print('B')
        B=floor
