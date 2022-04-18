class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        value = [([0]*m) for i in range(n)]
        # print(value)
        for i in range(n):
            for j in range(m):
                nj = (j+k)%m
                ni =  (i + (j+k)//m)%n
                value[ni][nj] = grid[i][j]
                # print(value)
        return value