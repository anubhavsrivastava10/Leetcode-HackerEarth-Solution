class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        total = sum(nums)
        val = 0
        ans = []
        for i in range(len(nums)-1,-1,-1):
            if(val>total):
                return ans
            else:
                val += nums[i]
                total -= nums[i]
                ans.append(nums[i])
        return ans