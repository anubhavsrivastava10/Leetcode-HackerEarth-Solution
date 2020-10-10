# Time complexity - O(n)
# Space complexity - O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val = float('inf')
        if len(prices)== 0 or len(prices)==1:
            return 0
        else:
            cost = 0
            for i in range(len(prices)):
                if val>prices[i]:
                    val = prices[i]
                elif cost < prices[i]-val:
                    cost = prices[i]-val
        return cost