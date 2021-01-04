class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''
        for item in s:
            z = ord(item)
            if z>=65 and z<=90:
                p += chr(z+32)
            elif z>=97 and z<=122:
                p += item
            elif z>=48 and z<=57:
                p += item
        if p == p[::-1]:
            return True
        return False