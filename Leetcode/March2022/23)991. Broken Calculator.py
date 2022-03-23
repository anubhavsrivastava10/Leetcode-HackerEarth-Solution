class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target>startValue:
            if target%2!=0:
                target+=1
                count+=1
            else:
                target = target//2
                count+=1
        if target==startValue:
            return count
        count += (startValue-target)
        return count