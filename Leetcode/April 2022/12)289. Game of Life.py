class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        for r in range(n):
            for c in range(m):
                count = 0
                for i,j in dirs:
                    nr = r+i
                    nc = c+j
                    if 0<=nr<n and 0<=nc<m and abs(board[nr][nc])==1:
                        count+=1
                if board[r][c]==1:
                    if count<2:
                        board[r][c] *= -1
                    elif count>3:
                        board[r][c] *= -1
                else:
                    if count==3:
                        board[r][c] = 2
        for r in range(n):
            for c in range(m):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
        return board
                    