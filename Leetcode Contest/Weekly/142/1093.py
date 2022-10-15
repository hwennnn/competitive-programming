# 1093. Statistics from a Large Sample
# https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = s = 0
        mp = collections.defaultdict(int)
        
        for i,x in enumerate(count):
            if x > 0:
                s += i * x
                mp[i] += x
                n += x
        
        mmin = min(mp)
        mmax = max(mp)
        mode = max(mp, key = mp.get)
        mean = s / n
        median = 0
        medianPos = (n // 2) if n % 2 != 0 else (n // 2 - 1, n // 2)
        
        if n & 1:
            curr = 0
            for key,v in mp.items():
                curr += v
                if curr > medianPos:
                    median = key
                    break
        else:
            curr = 0
            isNext = False
            for key, v in mp.items():
                if isNext:
                    median = (median + key) / 2
                    break
                curr += v
                if (curr > medianPos[0]):
                    if curr > medianPos[0] and curr <= medianPos[1]:
                        median = key
                        isNext = True
                    else:
                        median = key
                        break
            
        
        
        return [mmin, mmax, mean, median, mode]
