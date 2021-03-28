# 1807. Evaluate the Bracket Pairs of a String
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = collections.defaultdict(str)
        
        for k,v in knowledge:
            mp[k] = v
            
        res = []
        opened = None
        key = ""
        
        for i,x in enumerate(s):
            if x == "(": opened = i
                
            elif x == ")":
                if key not in mp:
                    res.append("?")
                else:
                    res.append(mp[key])
                key = ""
                opened = None
                continue
                
            if opened == None:
                res.append(x)
            else:
                if x != "(":
                    key += x
        
        return "".join(res)
