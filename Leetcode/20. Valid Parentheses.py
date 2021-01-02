class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            else:
                if stack == []:
                    return False
                else:
                    if stack[-1] == '(' and item == ')':
                        stack.pop()
                    elif stack[-1] == '{' and item == '}':
                        stack.pop()
                    elif stack[-1] == '[' and item == ']':
                        stack.pop()
                    else:
                        return False
        if stack==[]:
            return True
        return False