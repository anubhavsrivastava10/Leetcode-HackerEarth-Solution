class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count+=1
            lst.append([count,i])
        lst.sort()
        ans = []
        for i in range(k):
            ans.append(lst[i][1])
        return ans