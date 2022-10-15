# 2109. Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = set(spaces)
        
        for i, x in enumerate(s):
            if i in spaces:
                res.append(" ")
            
            res.append(x)
        
        return "".join(res)
