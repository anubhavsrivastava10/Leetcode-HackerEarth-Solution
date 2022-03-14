class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//","/")
        lst = path.split("/")
        stack = []
        for item in lst:
            if item=="..":
                if stack!=[]:
                    stack.pop()
            elif item=="." or item=="":
                continue
            else:
                stack.append(item)
        ans = ""
        print(stack)
        if stack==[]:
            return "/"
        for item in stack:
            ans += '/'
            ans+=item
        return ans