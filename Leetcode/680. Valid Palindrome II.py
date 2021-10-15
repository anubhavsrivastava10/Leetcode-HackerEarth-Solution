class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i,j=0,len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return s[i+1:j+1]==s[j:i:-1] or s[i:j]==s[j-1:i:-1]+s[i]
            i+=1
            j-=1