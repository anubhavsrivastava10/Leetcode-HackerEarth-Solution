class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [1]
        lst1 = [1,1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [lst]
        if numRows == 2:
            return [lst,lst1]
        else:
            arr = []
            arr.append(lst)
            arr.append(lst1)
            for i in range(2,numRows):
                lst = []
                for j in range(i-1):
                    lst.append(arr[-1][j]+arr[-1][j+1])
                lst.insert(0,1)
                lst.append(1)
                arr.append(lst)
            return arr
