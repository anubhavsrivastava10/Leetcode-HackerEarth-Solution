class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        def bt(visited, c):
            if len(c) == len(nums):                
                ans[(tuple(c))] = 1
                return
            for j, v2 in enumerate(nums):
                if j in visited:
                    continue
                visited.add(j)
                c.append(nums[j])
                bt(visited, c)
                visited.remove(j)
                c.pop()
        bt(set(), [])
        return ans