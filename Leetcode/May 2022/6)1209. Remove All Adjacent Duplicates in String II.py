class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack == []:
                stack.append([s[i],1])
            else:
                if stack[-1][0]==s[i]:
                    stack[-1][1] += 1
                    if stack[-1][1]==k:
                        stack.pop()
                else:
                    stack.append([s[i],1])
        ans = ""
        for item in stack:
            ans += item[0]*item[1]
        return ans