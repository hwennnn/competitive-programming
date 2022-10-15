# 1805. Number of Different Integers in a String
# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        
        tmp = ""
        for w in word+"a":
            if w in "12345667890":
                tmp += w
            else:
                if tmp != "":
                    while tmp and tmp[0] == "0":
                        tmp = tmp[1:]
                    s.add(tmp)
                tmp = ""
​
        return len(s)
