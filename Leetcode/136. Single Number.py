class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return []
        if len(nums) == 1: return nums.pop()
        t = nums.pop()
        
        while nums:
            t ^= nums.pop()
            
        return t
"""
## Other Solution 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for item in nums:
            if nums.count(item)==1:
                return item
"""