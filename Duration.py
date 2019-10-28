for i in range(0,int(input())):
    a = list(map(int, input().split()))
    hour = a[2]-a[0]
    minn = a[3]-a[1]
    if(minn<0):
        hour = hour-1
        minn = minn+60
    print(str(hour)+" "+str(minn))
