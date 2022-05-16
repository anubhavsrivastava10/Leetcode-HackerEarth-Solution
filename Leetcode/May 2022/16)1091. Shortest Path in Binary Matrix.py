class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        heap = [(1, 0, 0)] # length, starting_x, starting_y
        seen = set()
        seen.add((0, 0))
        while heap:
            length, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1): return length
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and grid[nx][ny] == 0:
                    seen.add((nx, ny))
                    heapq.heappush(heap, (length + 1, nx, ny))
        return -1