class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dick = {}
        cur = 0
        for item in nums:
            if item not in dick:
                dick[item] = 1
            else:
                dick[item] += 1
        for item in dick:
            if dick[item]>1:
                cur += (dick[item]*(dick[item]-1))//2
        return cur