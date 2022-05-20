class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        def solve(i , j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = solve(i + 1, j) + solve(i, j+1)
            return dp[i][j]
        
        return solve(0,0)