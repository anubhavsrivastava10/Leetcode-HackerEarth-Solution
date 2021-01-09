class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxx = 0
        for item in s:
            if item == '(':
                count += 1
                if count > maxx:
                    maxx = count
            elif item == ')':
                count -= 1
        return maxx