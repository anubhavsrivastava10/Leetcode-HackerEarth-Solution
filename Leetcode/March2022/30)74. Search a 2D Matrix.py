class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Optimal Solution
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = (m*n)-1
        while(start<=end):
            mid = start + (end-start)//2
            check = matrix[mid//n][mid%n]
            if(target<check):
                end = mid-1
            elif target>check:
                start = mid+1
            else:
                return True
        return False

        # Solution I wrote at first
        
        # for i in range(len(matrix)):
        #     if matrix[i][0]>target:
        #         i = i-1
        #         break
        #     elif matrix[i][0]==target:
        #         break
        # for j in range(len(matrix[i])):
        #     if matrix[i][j]==target:
        #         return True
        # return False