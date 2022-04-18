class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        start = 0
        for item in nums:
            total+=item
        total -= nums[0]
        for i in range(len(nums)):
            if i!=0:
                start += nums[i-1]
                total -= nums[i]
            # print(nums[i-1],nums[i])
            # print(start,total)
            if start==total:
                return i
        return -1