"""
Input Format:
The first line of the input contains two integers n and m --- the length of the array and constant number.
The second line of the input contains n numbers a1, a2, ..., an - the elements of the array.
The third line of the input contains m numbers h1, h2, ..., hm - the elements of the array.
The next line contains one number q - number of queries
The next q lines describe queries and contain two integers l, r
Output format:
For each query, print the answer --- 1, if subarray a[l..r] is happy and 0 otherwise
"""

m,n = map(int,input().split())
lst = list(map(int,input().split()))
ls = list(map(int,input().split()))
k = lst[1:]
for i in range(int(input())):
    l,r = map(int,input().split())
    z = lst[l-1:r]
    se = set(z)
    c=1
    for i in se:
        if z.count(i)==i:
            c=0
        else:
            c=1
            break
    if c==0:
        print(1)
    else:
        print(0)