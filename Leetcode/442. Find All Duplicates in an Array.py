class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for item in nums:
            if(nums[abs(item)-1]<0):
                ans.append(abs(item))
            else:
                nums[abs(item)-1] *= -1
        return ans