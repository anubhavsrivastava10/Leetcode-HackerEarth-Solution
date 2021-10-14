class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        new_num = num[::-1]
        for item in new_num:
            if int(item)%2!=0:
                break
            n-=1
        return num[:n]