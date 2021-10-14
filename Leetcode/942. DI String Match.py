class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        indx = 0
        lst = []
        for item in s:
            if item == "I":
                lst.append(indx)
                indx+=1
            else:
                lst.append(n)
                n-=1
        lst.append(indx)
        return lst