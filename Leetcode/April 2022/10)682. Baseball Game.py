class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        total = 0
        for item in ops:
            if item == "+":
                total += ans[-1]+ans[-2]
                ans.append(ans[-1]+ans[-2])
            elif item == "C":
                total -= ans.pop()
                # ans.pop()
            elif item == "D":
                total += ans[-1]*2
                ans.append(ans[-1]*2)
            else:
                ans.append(int(item))
                total += int(item)
        return total