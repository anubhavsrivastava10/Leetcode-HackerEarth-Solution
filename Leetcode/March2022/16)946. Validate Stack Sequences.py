class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i=0
        for item in pushed:
            stack.append(item)
            if i<len(popped):
                while stack[-1] == popped[i] and stack!= []:
                    # print(stack,i)
                    stack.pop()
                    i+=1
                    # print(stack,i)
                    if i==len(popped) or stack== []:
                        break
        if stack == []:
            return True
        return False