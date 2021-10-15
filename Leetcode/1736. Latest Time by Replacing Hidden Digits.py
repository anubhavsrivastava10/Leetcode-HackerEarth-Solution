class Solution:
    def maximumTime(self, time: str) -> str:
        new = ""
        if time[0]=="?":
            if time[1]=="?":
                new+="2"
            elif int(time[1])>3:
                new+="1"
            else:
                new+="2"
        else:
            new+=time[0]
        if time[1]=="?":
            if int(new[0])==1:
                new+="9"
            elif int(new[0])==2:
                new+="3"
            elif int(new[0])==0:
                new+="9"
        else:
            new+=time[1]
        new+=":"
        if time[3]=="?":
            new+="5"
        else:
            new += time[3]
        if time[4]=="?":
            new+="9"
        else:
            new+=time[4]
        
        return new