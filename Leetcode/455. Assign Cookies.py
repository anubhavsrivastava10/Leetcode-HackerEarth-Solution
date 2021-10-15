class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = 0
        n = len(s)
        count = 0
        for item in g:
            if(i>=n):
                break
            if item<=s[i]:
                count += 1
                i += 1
        return count