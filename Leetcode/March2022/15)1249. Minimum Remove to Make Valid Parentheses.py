class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        lst = list(s)
        for i in range(len(lst)):
            if lst[i] == "(":
                count += 1
            if lst[i] == ")":
                if count<=0:
                    lst[i] = ''
                else:
                    count -=1
        count = 0
        for i in range(len(lst)-1,-1,-1):
            if lst[i] == ")":
                count +=1
            if lst[i] == "(":
                if count<=0:
                    lst[i]=''
                else:
                    count -=1
        return ''.join(lst)