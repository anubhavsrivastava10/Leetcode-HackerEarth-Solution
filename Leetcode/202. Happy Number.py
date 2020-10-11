class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True
        else:
            su = n
            x = n
            while x>9:
                su = 0
                while x>0:
                    d = x%10
                    su += d*d
                    x = x//10
                if su==1:
                    return True
                x = su
            if su==7:
                return True
            return False