class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        check = [0]*26
        for i in range(len(s)):
            check[ord(s[i])-97] = i
        # print(check)
        start = 0
        end = 0
        ans = []
        for i in range(len(s)):
            end = max(end,check[ord(s[i])-97])
            if i==end:
                ans.append(i-start+1)
                start = i+1
        return ans