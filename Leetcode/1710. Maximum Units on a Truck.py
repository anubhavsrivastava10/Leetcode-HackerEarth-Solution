class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : -x[1])
        boxes = 0
        print(boxTypes)
        for numOfBoxes, unitsPerBox in boxTypes:
            toLoad = min(truckSize, numOfBoxes)
            truckSize -= toLoad
            boxes += toLoad*unitsPerBox
            if truckSize == 0:
                return boxes
        return boxes


# another Solution

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        lst = []
        for item in boxTypes:
            lst.append(item[1])
        t= 0
        val = 0
        # print(lst)
        while t<truckSize:
            a = lst.index(max(lst))
            # print(boxTypes[a])
            if lst[a]!=-1:
                if t+boxTypes[a][0] <= truckSize:
                    t += boxTypes[a][0]
                    val += boxTypes[a][0]*boxTypes[a][1]
                else:
                    b = truckSize-t
                    t += boxTypes[a][0]
                    val += b*boxTypes[a][1]
            else:
                break
            lst[a] = -1
        return val