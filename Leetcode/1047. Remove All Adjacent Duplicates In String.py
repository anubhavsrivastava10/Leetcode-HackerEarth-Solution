class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if stack==[]:
                stack.append(item)
            else:
                if item==stack[-1]:
                    stack.pop()
                else:
                    stack.append(item)
        ans = ""
        for item in stack:
            ans += item
        return ans