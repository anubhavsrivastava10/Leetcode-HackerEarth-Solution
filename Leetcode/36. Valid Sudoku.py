class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums_row = [x for x in row if x != "."]
            if len(set(nums_row)) != len(nums_row):
                return False
            
        for col in zip(*board):
            nums_col = [x for x in col if x != "."]
            if len(set(nums_col)) != len(nums_col):
                return False
        
        for i in range(0,9,3):
            for j in range(0, 9, 3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[i + k][j + l])
                nums_square = [x for x in square if x != "."]
                if len(set(nums_square)) != len(nums_square):
                    return False
        
        return True