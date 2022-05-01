class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        res = 0
        pq = [(0, 0, 0)]
        while True:
            res , x, y = heappop(pq)
            if heights[x][y] == -1:
                continue
            if x == m-1 and y==n-1:
                return res
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny]!=-1:
                    heappush(pq, (max(res, abs(heights[x][y] - heights[nx][ny])), nx, ny))
            heights[x][y] = -1
        return -1
                