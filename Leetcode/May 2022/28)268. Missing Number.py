class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for item in nums:
            total += item
            count +=1
        return ((count*(count+1)//2)-total)