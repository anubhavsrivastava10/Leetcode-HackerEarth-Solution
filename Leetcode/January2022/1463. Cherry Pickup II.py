class Solution(object):
    def cherryPickup(self, grid):
        ROW_NUM = len(grid)
        COL_NUM = len(grid[0])

        dp = [[[0] * COL_NUM for _ in grid[0]] for _ in grid]
        # fulfill dp of the last row
        for i in range(COL_NUM):
            for j in range(COL_NUM):
                dp[-1][i][j] = grid[-1][i] if i == j else grid[-1][i] + grid[-1][j]

        # from the second last row to the first row
        for k in range(ROW_NUM - 2, -1, -1):
            row = grid[k]
            for i in range(COL_NUM):
                for j in range(i, COL_NUM):
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if 0 <= i + di < COL_NUM and 0 <= j + dj < COL_NUM:
                                if i == j:  # they can only pickup once
                                    dp[k][i][j] = max(dp[k][i][j], dp[k + 1][i + di][j + dj] + row[i])
                                else:
                                    dp[k][i][j] = max(dp[k][i][j], dp[k + 1][i + di][j + dj] + row[i] + row[j])
        return dp[0][0][COL_NUM - 1]
class Solution(object):
    def cherryPickup(self, grid):
        def dp(k):
            if k == ROW_NUM - 1:  # the last row
                return [[grid[-1][i] if i == j else grid[-1][i] + grid[-1][j] for j in range(COL_NUM)]
                        for i in range(COL_NUM)]

            row = grid[k]
            ans = [[0] * COL_NUM for i in range(COL_NUM)]
            next_dp = dp(k + 1)  # get result if next row
            for i in range(COL_NUM):
                for j in range(i, COL_NUM):
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if 0 <= i + di < COL_NUM and 0 <= j + dj < COL_NUM:
                                if i == j:  # they can only pickup once
                                    ans[i][j] = max(ans[i][j], next_dp[i + di][j + dj] + row[i])
                                else:
                                    ans[i][j] = max(ans[i][j], next_dp[i + di][j + dj] + row[i] + row[j])
            return ans

        ROW_NUM = len(grid)
        COL_NUM = len(grid[0])
        return dp(0)[0][COL_NUM - 1]
