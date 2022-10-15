# 1904. The Number of Full Rounds You Have Played
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        stt = startTime.split(":")
        ftt = finishTime.split(":")
        st = int("".join(stt))
        ft = int("".join(ftt))
​
        mm = 0
        overnight = (int(ftt[0]) <= int(stt[0]) and int(ftt[1]) <= int(stt[1]))
        
        if overnight:
            h = 24 - int(stt[0])
            h += int(ftt[0])
​
            if h > 0:
                h -= 1
                mm += h * 4
                hh = (int(stt[0]) + h) % 24
                stt[0] = "0" + str(hh) if hh < 10 else str(hh)
        
        def getNext(x):
            if 0 <= x < 15: return "15"
            if 15 <= x < 30: return "30"
            if 30 <= x < 45: return "45"
            
            return "00"
​
​
        while int(stt[0]) != int(ftt[0]) or int(stt[1]) != int(ftt[1]):
            if int(stt[0]) == int(ftt[0]) and int(stt[1]) + 15 > int(ftt[1]): break
​
            if stt[1] in ["00", "15", "30", "45"]:
                mm += 1
​
            nxt = getNext(int(stt[1]))
            stt[1] = nxt
            if stt[1] == "00":
                stt[0] = str(int(stt[0]) + 1) if int(stt[0]) < 23 else "00"
        
        return mm
