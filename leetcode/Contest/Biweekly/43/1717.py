# 1717. Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int):
        a = b = res = 0
        
        if x == y:
            for i,c in enumerate(s):
                if c == "a": 
                    if b > 0:
                        res += y
                        b -= 1
                    else:
                        a += 1

                elif c == "b": 
                    if a > 0:
                        res += x
                        a -= 1
                    else:
                        b += 1

                else: 
                    a = b = 0
        else:
            checkAB = x > y
            used = set()
            adeq = deque()
            bdeq = deque()
            
            for i,c in enumerate(s):
                if c == "a":
                    if checkAB:
                        a += 1
                        adeq.append(i)
                    else:
                        if b > 0:
                            res += y
                            b -= 1
                            used.add(bdeq.pop())
                            used.add(i)
                        else:
                            a += 1
                            adeq.append(i)
                            
                elif c == "b":
                    if checkAB:
                        if a > 0:
                            res += x
                            a -= 1
                            used.add(adeq.pop())
                            used.add(i)
                        else:
                            b += 1
                            bdeq.append(i)
                    else:
                        b += 1
                        bdeq.append(i)
                            
                else:
                    a = b = 0
                    adeq.clear()
                    bdeq.clear()
                    
            a = b = 0
            
            for i,c in enumerate(s):
                if c != "a" and c != "b":
                    a = b = 0
                else:
                    if i in used: continue
                        
                    if c == "a": 
                        if b > 0:
                            res += y
                            b -= 1
                        else:
                            a += 1

                    else: 
                        if a > 0:
                            res += x
                            a -= 1
                        else:
                            b += 1
                    
                    
        
        return res

                
            
        
        