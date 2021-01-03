class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst = []
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[n+i])
        return lst