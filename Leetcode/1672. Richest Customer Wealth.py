class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        val = 0
        for item in accounts:
            p = sum(item)
            if p > val:
                val = p
        return val