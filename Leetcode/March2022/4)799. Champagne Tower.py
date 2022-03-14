class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0 for j in range(x)] for x in range(1, query_row + 2)]
        tower[0][0] = poured
        for i in range(query_row):
            for j in range(len(tower[i])):
                temp = (tower[i][j] - 1) / 2.0
                if temp>0:
                    tower[i+1][j] += temp
                    tower[i+1][j+1] += temp
                    
        if tower[query_row][query_glass] <= 1:
            return tower[query_row][query_glass]
        else:
            return 1
