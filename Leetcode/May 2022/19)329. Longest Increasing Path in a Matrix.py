class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        directions = [0, 1, 0, -1, 0]
        @lru_cache(maxsize=None)
        def dfs(r,c):
            ans=1
            for i in range(4):
                new_row,new_col=r+directions[i], c+directions[i+1]
                if 0<=new_row<m and 0<=new_col<n and matrix[new_row][new_col]>matrix[r][c]:
                    ans = max(ans, dfs(new_row, new_col) + 1 )
            return ans
        return max(dfs(r,c) for r in range(m) for c in range(n))