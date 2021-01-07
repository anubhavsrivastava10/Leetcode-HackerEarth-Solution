class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = ['']*len(indices)
        i = 0
        final = ''
        for item in indices:
            lst[item] = s[i]
            i+=1
        return final.join(lst)