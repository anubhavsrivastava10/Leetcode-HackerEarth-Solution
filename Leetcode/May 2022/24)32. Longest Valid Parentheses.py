class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        l,r=0,0
        for i in range(len(s)):
            if s[i] == '(':
                l+=1
            else:
                r+=1
            if l == r:
                max_length=max(max_length, l*2)
            elif r>l:
                l=r=0
        l,r=0,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l+=1
            else:
                r+=1
            if l == r:
                max_length=max(max_length, l*2)
            elif l>r:
                l=r=0
        return max_length