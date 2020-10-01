for _ in range(int(input())):
    n,m,d = map(str,input().split())
    bin_ = '{0:016b}'.format(int(n))
    n = str(bin_)
    if d=='L':
        for i in range(int(m)):
            n = n[1:]+n[0]
    else:
        for i in range(int(m)):
            n = n[-1]+n[:-1]
    print(int(n,2))