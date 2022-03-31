class Solution:        
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(mid) -> bool:
            s = 0
            div = 1
            for item in nums:
                s += item
                if s > mid:
                    div += 1
                    s = item
                    if div > m:
                        return False
            return True
        
        min_val = max(nums)
        max_val = sum(nums)
        
        while(min_val<max_val):
            mid = min_val + (max_val-min_val)//2
            if(split(mid)):
                max_val = mid
            else:
                min_val = mid+1
        return min_val
    
    