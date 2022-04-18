class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for item in nums:
            if item in dic:
                dic[item]+=1
            else:
                dic[item]=1
        lst = []
        for item in dic:
            lst.append([dic[item],item])
        lst.sort(reverse=True)
        ans = []
        # print(lst)
        i = 0
        while(k>0):
            k-=1
            ans.append(lst[i][1])
            i+=1
        return ans