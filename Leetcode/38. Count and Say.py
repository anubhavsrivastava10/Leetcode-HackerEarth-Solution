class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        s = '1'
        for i in range(n-1):
            previous,count = s[0],0
            new = ''
            for current in s:
                if previous != current:
                    new += str(count) + previous
                    previous,count = current,1
                else:
                    count += 1    
            new += str(count) + previous
            s = new
        return s