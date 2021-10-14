class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for item in bills:
            if item == 5:
                five += 1
            elif item == 10:
                if five>0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif item == 20:
                if ten>0 and five>0:
                    ten -= 1
                    five -= 1
                elif five > 3:
                    five -= 3
                else:
                    return False
        return True
                
                    