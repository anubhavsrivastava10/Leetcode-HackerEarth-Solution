class Solution(object):
    def isRobotBounded(self, I):
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        di = x = y = 0
        for i in I:
            if i == 'L': di = (di + 1) % 4
            elif i == 'R': di = (di - 1) % 4
            else: x, y = x + d[di][0], y + d[di][1]
        if x == 0 and y == 0 or di > 0: return True
        return False
