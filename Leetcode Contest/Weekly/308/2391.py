# 2391. Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        lastM = lastP = lastG = -1
        M, P, G = [0] * n, [0] * n, [0] * n
        
        for index, gar in enumerate(garbage):
            c = Counter(gar)
            M[index] += c["M"]
            P[index] += c["P"]
            G[index] += c["G"]
        
            if c["M"] > 0:
                lastM = index
            
            if c["P"] > 0:
                lastP = index
            
            if c["G"] > 0:
                lastG = index
        
        mCount = 0
        if lastM != -1:
            for index in range(0, lastM + 1):
                mCount += M[index]
                if index != lastM:
                    mCount += travel[index]
​
        pCount = 0
        if lastP != -1:
            for index in range(0, lastP + 1):
                pCount += P[index]
                if index != lastP:
                    pCount += travel[index]
​
        gCount = 0
        if lastG != -1:
            for index in range(0, lastG + 1):
                gCount += G[index]
                if index != lastG:
                    gCount += travel[index]                
        
        return mCount + pCount + gCount
            
        
