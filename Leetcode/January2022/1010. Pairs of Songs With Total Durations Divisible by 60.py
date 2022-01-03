class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        lst = [0]*60
        count = 0
        for t in time:
            rem = t%60
            val = (60-rem)%60
            count += lst[val]
            lst[rem]+=1
        return count
