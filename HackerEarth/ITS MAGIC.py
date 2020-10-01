    x = int(input())
    lst = list(map(int,input().split()))
    ls = sorted(lst)
    k=-1
    summ = sum(lst)
    for i in range(x):
        z = summ-ls[i]
        if z%7==0:
            k = ls[i]
            break
    if k!=-1:
        print(lst.index(k))
    else:
        print(k)