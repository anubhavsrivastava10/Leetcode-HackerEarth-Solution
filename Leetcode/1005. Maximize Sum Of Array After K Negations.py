class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        flag = 0
        val = k
        if(len(nums)<k):
            val = len(nums)
        for i in range(val):
            if nums[i]<0:
                nums[i] = abs(nums[i])
            elif nums[i]==0:
                flag = 1
                break
            else:
                break
            count += 1
            
        nums.sort()
        if flag==1:
            return sum(nums)
        else:
            if(count==k):
                return sum(nums)
            elif (k-count)%2==0:
                return sum(nums)
            else:
                return sum(nums)-nums[0]-nums[0]