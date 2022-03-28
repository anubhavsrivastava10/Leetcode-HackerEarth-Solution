class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for item in arr:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        checkSet = set()
        # print(hashmap)
        for item in hashmap:
            if hashmap[item] not in checkSet:
                checkSet.add(hashmap[item])
            else:
                return False
        return True