class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        alpha = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        for item in alpha[digits[0]]:
            ans.append(item)
        n = len(digits)
        for i in range(1,n):
            total = []
            for item in ans:
                for val in alpha[digits[i]]:
                    total.append(item+val)
                ans = total
        return ans