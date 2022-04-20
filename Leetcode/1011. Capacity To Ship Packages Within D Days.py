class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        mid = (start+end)//2
        check = 0
        while(start<=end):
            mid = (start+end)//2
            # print(start,end,mid)
            count = 1
            ans = 0
            for item in weights:
                ans += item
                if ans > mid:
                    ans = item
                    count+=1
            if count > days:
                start = mid+1
            elif count <= days:
                check = mid
                end = mid-1
        return check