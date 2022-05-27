class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChangeInner(rem, cache):
            if rem < 0:
                return math.inf
            if rem == 0:                    
                return 0       
            if rem in cache:
                return cache[rem]
            
            cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)                         
            return cache[rem]      
        
        ans = coinChangeInner(amount, {})
        return -1 if ans == math.inf else ans