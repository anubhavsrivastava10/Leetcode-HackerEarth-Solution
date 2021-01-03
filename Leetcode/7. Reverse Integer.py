class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        if x>0:
            val = 0
            while x>0:
                n = x%10
                val *= 10
                val += n
                x = x//10
                if val>(2**31)-1:
                    return 0
            return val
        if x<0:
            val = 0
            x = x*-1
            while x>0:
                n = x%10
                val *= 10
                val += n
                x = x//10
                if val>(2**31)-1:
                    return 0
            val = val*-1
            return val
