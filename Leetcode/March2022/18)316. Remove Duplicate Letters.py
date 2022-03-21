class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        stack = []
        for i in range(len(s)):
            last_occ[s[i]] = i
        for i in range(len(s)):
            if s[i] not in stack:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    stack.pop()
                stack.append(s[i])
        return ''.join(stack)