class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=0
        i=1
        while(i<len(nums)):
            if nums[i-1]!=nums[i]:
                p+=1
                nums[p]=nums[i]
            i+=1
        del nums[p+1:]
        return len(nums)