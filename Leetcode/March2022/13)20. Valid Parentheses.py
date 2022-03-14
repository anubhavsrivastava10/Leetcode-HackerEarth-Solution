class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            else:
                if stack == []:
                    return False
                if item==')' and stack[-1]=='(':
                    stack.pop()
                elif item=='}' and stack[-1]=='{':
                    stack.pop()
                elif item==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            # print(stack)
        if stack==[]:
            return True
        return False