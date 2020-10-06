class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            l = len(digits)-1
            while digits[l]==9 and l>=0:
                digits[l]=0
                l-=1
            if l< 0:
                return [1]+digits
            else:
                digits[l]+=1
                return digits