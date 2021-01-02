# This is a fibonacci series
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n<=1:
            return 1
        elif n==2:
            return 2
        else:
            # val = 0
            for i in range(n-2):
                a,b = b,a+b
            return b