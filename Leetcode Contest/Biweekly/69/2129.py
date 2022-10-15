# 2129. Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split(" ")
        
        res = []
        
        for word in s:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word.capitalize())
        
        return " ".join(res)
