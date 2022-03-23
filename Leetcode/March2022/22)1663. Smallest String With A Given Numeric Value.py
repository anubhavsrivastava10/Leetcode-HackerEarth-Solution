class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ''
        lst = []
        for i in range(26):
            lst.append(chr(97+i))
        for i in range(n,0,-1):
            val = k-i+1
            if val>=26:
                ans+=lst[25]
                k = k-26
            else:
                ans += lst[val-1]
                k = k-val
        return ans[::-1]