class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        up = defaultdict(int)
        down = defaultdict(int)
        same = defaultdict(int)
        for i in range(len(tops)):
            up[tops[i]] += 1
            down[bottoms[i]] += 1
            if tops[i]==bottoms[i]:
                same[tops[i]] += 1
        ans = float('inf')
        for i in range(1,7):
            if up[i]+down[i]-same[i]==len(tops):
                check = min(up[i],down[i])
                ans = min(ans,check-same[i])
        if ans==float('inf'):
            return -1
        return ans