class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        for item in trips:
            arr.append([item[1],item[0]])
            arr.append([item[2],item[0]*-1])
        total = 0
        print(arr)
        arr.sort()
        for item in arr:
            total += item[1]
            if total>capacity:
                return False
        return True
