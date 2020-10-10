class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for item in nums:
            if item==i:
                i+=1
            else:
                return i
        return i