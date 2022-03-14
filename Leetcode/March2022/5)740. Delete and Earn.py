class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        lst = [0]*100001
        for item in nums:
            lst[item] += 1
        ans = [0]*100001
        ans[1] = lst[1]
        for i in range(2,100001):
            ans[i] = max(ans[i-2]+(i*lst[i]),ans[i-1])
        return ans[100000]