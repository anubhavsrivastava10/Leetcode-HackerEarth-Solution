class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # lst= []
        # if len(nums)<3:
        #     return 0
        # diff = nums[1]-nums[0]
        # count = 1
        # for i in range(0,len(nums)-1):
        #     if nums[i+1]-nums[i] == diff:
        #         # print(nums[i+1],nums[i])
        #         count+=1
        #     else:
        #         diff = nums[i+1]-nums[i]
        #         # print(diff)
        #         lst.append(count)
        #         count = 2
        # lst.append(count)
        # print(lst)
        # ans = 0
        # for item in lst:
        #     ans += (item*(item-1))-(((item*(item+1))//2)-1)
        # return ans
        if len(nums)<3:
            return 0
        ans = 0
        for i in range(len(nums)-1):
            diff = nums[i+1]-nums[i]
            for j in range(i+2,len(nums)):
                if nums[j]-nums[j-1]==diff:
                    ans+=1
                else:
                    break
        return ans