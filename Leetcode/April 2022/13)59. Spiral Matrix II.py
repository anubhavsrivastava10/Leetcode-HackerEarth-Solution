class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rs = 0
        re = n-1
        cs = 0
        ce = n-1
        lst = [[0]*n for j in range(n)]
        count = 1
        while rs<=re and cs<=ce:
            
            #move from left to right
            for i in range(cs,ce+1):
                lst[rs][i] = count
                count += 1
                
            for i in range(rs+1,re+1):
                lst[i][ce] = count
                count += 1
                
            for i in range(ce-1,cs-1,-1):
                lst[re][i] = count
                count += 1
            
            for i in range(re-1,rs,-1):
                lst[i][cs] = count
                count += 1
                
            rs += 1
            re -= 1
            cs += 1
            ce -= 1
        
        return lst