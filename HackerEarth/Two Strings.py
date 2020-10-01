for i in range(0,int(input())):
    x = input().split(" ")
    if sorted(list(x[0]))==sorted(list(x[1])):
        print('YES')
    else:
        print('NO')
