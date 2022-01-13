class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda points: points[1])
        print(points)
        count = 1
        shoot = points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=shoot:
                continue
            else:
                count+=1
                shoot = points[i][1]
        return count
