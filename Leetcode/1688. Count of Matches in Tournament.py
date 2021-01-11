class Solution:
    def numberOfMatches(self, n: int) -> int:
        val = 0
        while n>1:
            if n%2==0:
                n = n//2
                val += n
            else:
                n = ((n-1)//2)+1
                val += n-1
        return val