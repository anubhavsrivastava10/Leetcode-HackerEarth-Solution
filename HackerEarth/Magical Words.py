prime =  []
for i in range(65,91):
    count = 0
    for j in range(1,i):
        if i%j == 0:
            count += 1
    if count == 1:
        prime.append(i)
for i in range(97,123):
    count = 0
    for j in range(1,i):
        if i%j == 0:
            count += 1
    if count == 1:
        prime.append(i)
 
 
l = len(prime)
t = int(input())
for i in range(0,t):
    n = int(input())
    out = ['a']*n
    alp = str(input())
    for j in range(0,n):
        a = ord(alp[j])
        d = 255
        for k in range(0,l):
            if abs(prime[k] - a) < d:
                d = abs(prime[k] - a)
                out[j] = chr(prime[k])
    for x in range(0,n):
        print(out[x],end ="")
    print('')