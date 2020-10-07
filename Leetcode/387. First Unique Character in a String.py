# you can also use dictionary instead of list here
# but the main idea will be the same 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = [0]*26
        for item in s:
            if lst[ord(item)-97]==0:
                lst[ord(item)-97] += 1
            else:
                lst[ord(item)-97] = -1
        for i in range(len(s)):
            if lst[ord(s[i])-97] == 1:
                return i
        return -1