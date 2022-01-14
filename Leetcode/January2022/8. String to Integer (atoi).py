class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s=="":
            return 0
        else:
            plus = 0
            minus = 0
            new = ""
            flag = 0
            for item in s:
                if item=="+":
                    if flag==1 or plus==1:
                        break
                    plus = 1
                elif item=="-":
                    if flag==1 or minus==1:
                        break
                    minus = 1
                elif item.isdigit():
                    new+=item
                    flag=1
                else:
                    break
            if new=="":
                return 0
            elif plus==1 and minus==1:
                return 0
            elif plus==1:
                return min(int(new), (1<<31)-1)
            elif minus==1:
                return max(-int(new), -(1<<31))
            else:
                return min(int(new), (1<<31)-1)
