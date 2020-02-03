from math import floor,ceil
for i in range(int(input())):
    n,a,b=map(int, input().split())
    x0=ceil((b*n)/(a+b))
    x1=floor((b*n)/(a+b))
    y0=n-x0
    y1=n-x1
    su1=(a*x0*x0+b*y0*y0)
    su2=(a*x1*x1+b*y1*y1)
    print(min(su1,su2))
