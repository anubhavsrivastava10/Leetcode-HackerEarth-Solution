class Solution:
    def twoSum(self, arr: List[int], targetSum: int) -> List[int]:
            hash=[]
            count=0
            for i in range(len(arr)):
                potential_sum = targetSum-arr[i]
                if (potential_sum) in hash:
                    return [hash.index(potential_sum),i]
                else:
                    hash.append(arr[i])