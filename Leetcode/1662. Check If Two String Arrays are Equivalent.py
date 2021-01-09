class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''
        str2 = ''
        for item in word1:
            str1 += item
        for item in word2:
            str2 += item
        return str1==str2