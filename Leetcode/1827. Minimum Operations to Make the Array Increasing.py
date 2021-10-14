class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = 0
        for i in range(1,len(nums)):
            if(nums[i-1]>=nums[i]):
                count = nums[i-1]-nums[i]+1
                nums[i]+=count
                total += count
        return total