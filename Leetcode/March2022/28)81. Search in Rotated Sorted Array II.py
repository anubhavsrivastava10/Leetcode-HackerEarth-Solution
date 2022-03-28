class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if target in nums:
        #     return True
        # return False
        start = 0
        end = len(nums)-1
        mid = 0
        while(start<end):
            mid=(start+end)//2;
            if(nums[mid]==target):
                return True
            if(nums[mid]>nums[end]):
                if(nums[mid]>target and nums[start] <= target):
                    end = mid
                else:
                    start = mid + 1
            elif(nums[mid] < nums[end]):
                if(nums[mid]<target and nums[end] >= target):
                    start = mid + 1
                else:
                    end = mid
            else:
                end -= 1
        if nums[start] == target:
            return True
        return False
