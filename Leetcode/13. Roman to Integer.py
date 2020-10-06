class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i, x in enumerate(s[:-1]):
            if dic[x] < dic[s[i + 1]]:
                val -= dic[x]
            else:
                val += dic[x]

        return val + dic[s[-1]]