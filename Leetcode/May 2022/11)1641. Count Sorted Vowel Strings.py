class Solution:
    def countVowelStrings(self, n: int) -> int:
        lst = [1]*5
        ans = 0
        while(n):
            n-=1
            for i in range(3,-1,-1):
                lst[i] += lst[i+1]
            # print(lst)
        return lst[0]
        