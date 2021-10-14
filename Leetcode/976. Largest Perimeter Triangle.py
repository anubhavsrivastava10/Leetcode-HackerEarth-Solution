class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        for i in range(len(nums)-2):
            flag = 0
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if(a+b<=c):
                flag = 1
                continue
            elif(b+c<=a):
                flag = 1
                continue
            elif(a+c<=b):
                flag = 1
                continue
            if(flag==0):
                return a+b+c
        return 0