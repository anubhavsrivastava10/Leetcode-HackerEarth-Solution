class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        start = 0
        end = n-1
        mid = (start+end)//2
        lst = []
        while(start<=end):
            # print(mid)
            if nums[mid]==target:
                while(mid>0 and nums[mid-1]==target):
                    mid-=1
                # print(mid)
                while(mid<n and nums[mid]==target):
                    lst.append(mid)
                    mid+=1
                break
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
            mid = (start+end)//2
        return lst
                
        