class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        lst = set()
        nums.sort()
        for i in range(n-2):
            # print(nums[i])
            start = i+1
            end = n-1
            while(start<end):
                if nums[i]+nums[start]+nums[end]==0:
                    lst.add((nums[i],nums[start],nums[end]))
                    start+=1
                    end-=1
                elif nums[i]+nums[start]+nums[end]<0:
                    start+=1
                elif nums[i]+nums[start]+nums[end]>0:
                    end-=1
        return lst