class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for item in position:
            if item%2==0:
                even+=1
            else:
                odd+=1
        if(even>=odd):
            return odd
        else:
            return even