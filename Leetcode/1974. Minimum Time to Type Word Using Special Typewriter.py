class Solution:
    def minTimeToType(self, word: str) -> int:
        n = len(word)
        indx = 0
        total = 0
        for i in range(n):
            val = ord(word[i])-97
            if(abs(val-indx)>26-abs(val-indx)):
                total += 26-abs(val-indx)
                total += 1
                indx = val
            else:
                total += abs(val-indx)
                total += 1
                indx = val
        return total
                 