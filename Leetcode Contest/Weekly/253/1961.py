# 1961. Check If String Is a Prefix of Array
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ss = ""
        n = 0
        
        for word in words:
            n += len(word)
            ss += word
​
            if s[:n] != ss:
                ss = ss[:n - len(word)]
                return ss == s
            
        return ss == s
