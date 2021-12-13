class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        value = 1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            else:
                if(value<count):
                    value = count
                count = 1
        if(value<count):
            value = count    
        return value