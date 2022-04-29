class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 10000
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            start = i+1
            end = n-1
            while(start<end):
                s = nums[i]+nums[start]+nums[end]
                if s >= target:
                    end -= 1
                elif s < target:
                    start += 1
                if(abs(s-target)<abs(ans-target)):
                    ans = s
        return ans