class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        count = 0
        rel = 0
        sum_needed = total//3
        if total%3!=0:
            return False
        for item in arr:
            rel+=item
            if rel==sum_needed:
                count+=1
                rel = 0
            if count==3:
                return True
        return count==3