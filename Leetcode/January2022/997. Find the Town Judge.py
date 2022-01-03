class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        lst = [0]*(n+1)
        for item in trust:
            lst[item[0]]-=1
            lst[item[1]]+=1
        print(lst)
        for i in range(1,n+1):
            if lst[i]==n-1:
                return i
        print(lst)
        return -1
