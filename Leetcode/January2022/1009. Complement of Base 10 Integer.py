class Solution:
    def bitwiseComplement(self, n: int) -> int:
        val = bin(n)
        val = val[2:]
        new = 0
        for item in val:
            if item == '1':
                new *= 10
                new += 0
            else:
                new *= 10
                new += 1
        count = 0
        ans = 0
        while(new>0):
            rem = new%10
            new = new//10
            ans += (2**count)*rem
            count+=1
        return ans

    
# A better approach will be as follows
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans = 1
        while n > ans:
            ans = ans * 2 + 1
        return ans - n
