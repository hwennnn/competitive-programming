# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        i = res = 0
        
        for j,x in enumerate(s):
            if x not in mp:
                mp.add(x)
            else:
                while x in mp:
                    mp.remove(s[i])
                    i += 1
                mp.add(x)
            
            res = max(res, len(mp))
        
        return res