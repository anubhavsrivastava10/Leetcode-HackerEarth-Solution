class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        num = [1,2,3,4,5,6,7,8,9]
        def backTrack(i,cur):
            if len(cur) == k:
                if sum(cur) == n:
                    res.append(list(cur))
            else:
                for j in range(i,len(num)):
                    cur.append(num[j])
                    backTrack(j+1,cur)
                    cur.pop()
        res = []
        backTrack(0,[])
        return res