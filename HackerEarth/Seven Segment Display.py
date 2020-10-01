def solve(S):
    map_ = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}
    
    num = 0
    for c in S:
        num += map_[c]
    res = ''        
    while num > 0:
        if num & 1 == 1:
            res += '7'
            num -= 3
        else:
            res += '1'
            num -= 2
    return res
    
T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
