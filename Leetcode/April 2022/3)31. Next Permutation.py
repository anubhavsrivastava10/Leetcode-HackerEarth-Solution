class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        indx = n-1
        while(indx>0):
            if(nums[indx-1]<nums[indx]):
                break
            indx -= 1
        if indx==0:
            for i in range(n//2):
                nums[i],nums[n-i-1] = nums[n-1-i],nums[i]
        else:
            j = n-1
            val = nums[indx-1]
            while(j>=indx):
                if nums[j]>val:
                    break
                j -= 1
            nums[j], nums[indx-1] = nums[indx-1], nums[j]
            # print(nums)
            # print(indx)
            if indx>n-1:
                return
            start = indx
            end = n-1
            for i in range(start, ((start+end)//2)+1):
                # print(nums)
                nums[i], nums[start+end-i] = nums[start+end-i], nums[i]