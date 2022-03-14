class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        k = len(s)
        if k==0:
            return True
        for item in t:
            if item == s[i]:
                i+=1
            if i==k:
                return True
        return False
            