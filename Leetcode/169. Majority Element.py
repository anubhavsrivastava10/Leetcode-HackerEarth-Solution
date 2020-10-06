class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        x = len(nums)
        for item in nums:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item]+=1
        for item in dic:
            if dic[item]>x//2:
                return item
                