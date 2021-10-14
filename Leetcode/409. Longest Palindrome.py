class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for item in s:
            if item in dic:
                dic[item]+=1
            else:
                dic[item]=1
        length = 0
        m = 0
        flag = 0
        for item in dic:
            if dic[item]%2==0:
                length += dic[item]
            else:
                length += dic[item]-1
                flag = 1
        if flag == 1:
            length += 1
        return length