# 1718. Construct the Lexicographically Largest Valid Sequence
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution:
    def constructDistancedSequence(self, n: int):
        length = 1 + (n-1)*2
        res = [0] * length
        used = set()
        
        def backtrack(idx):
            if idx == length: return True
            
            if res[idx]:
                if backtrack(idx+1):
                    return True
                return False
            
            for i in range(n, 0, -1):
                if i in used: continue
                
                if i == 1:
                    res[idx] = i
                    used.add(i)
                    
                    if backtrack(idx+1): return True
                    
                    res[idx] = 0
                    used.remove(i)
                
                else:
                    if i + idx >= length or res[i+idx]:
                        continue
                        
                    res[idx] = i
                    res[idx+i] = i
                    used.add(i)
                    
                    if backtrack(idx+1): return True
                    
                    res[idx] = 0
                    res[idx+i] = 0
                    used.remove(i)
            
            return False
        
        backtrack(0)
        return res