class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst = [0]*26
        for i in range(len(s)):
            lst[ord(s[i])-97] += 1
        for i in range(len(t)):
            lst[ord(t[i])-97] -= 1
        if lst.count(0)==26:
            return True
        else:
            return False