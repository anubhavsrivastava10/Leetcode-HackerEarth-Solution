class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        i =0
        while i <(len(s)-2):
            if s[i]==s[i+1]==s[i+2]=="O":
                i+=3
                continue
            elif s[i]=="O":
                i+=1
                continue
            else:
                count+=1
                i+=3
        if(i<len(s)):
            while i<len(s):
                if s[i]=="X":
                    count+=1
                    break
                i+=1
        return count