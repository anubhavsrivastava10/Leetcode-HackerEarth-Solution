# This solution takes O(n) time
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for item in nums:
            if item in hashmap:
                if hashmap[item]>0:
                    count += 1
                    hashmap[item]-=1
                else:
                    final = k-item
                    if final not in hashmap:
                        hashmap[final] = 1
                    else:
                        hashmap[final] += 1
            else:
                final = k-item
                if final not in hashmap:
                    hashmap[final] = 1
                else:
                    hashmap[final] += 1
        return count

# I will just tidy things up in the above solution
# Instead of finding the array element in the hashmap I will find the difference and store the element
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for item in nums:
            final = k - item 
            if final in hashmap:
                count += 1
                if hashmap[final]==1:
                    del hashmap[final]
                else:
                    hashmap[final] -= 1
            else:
                if item in hashmap:
                    hashmap[item] += 1
                else:
                    hashmap[item] = 1
        return count

# This solution takes O(nLog(n)) time
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        count = 0
        while i<j:
            if nums[i]+nums[j]==k:
                count+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            elif nums[i]+nums[j]>k:
                j-=1
        return count