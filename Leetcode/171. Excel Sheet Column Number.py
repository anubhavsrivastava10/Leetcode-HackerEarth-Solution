class Solution:
    def titleToNumber(self, s: str) -> int:
        count = len(s)-1
        val = 0
        for item in s:
            val += 26**count * (ord(item)-64)
            count-=1
        return val