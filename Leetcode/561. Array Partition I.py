class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        indx = 0
        nums.sort()
        total = 0
        for item in nums:
            if indx%2==0:
                total+=item
            indx+=1
        return total