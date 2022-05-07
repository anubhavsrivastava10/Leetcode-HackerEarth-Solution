class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        low = -float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<low:
                return True
            while(stack!=[] and stack[-1]<nums[i]):
                low = stack.pop()
            stack.append(nums[i])
        return False