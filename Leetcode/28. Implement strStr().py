class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle in haystack:
            indx = haystack.find(needle)
            return indx
        else:
            return -1
        return -1