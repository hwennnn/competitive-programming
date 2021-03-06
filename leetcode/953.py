# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
​
        return (all(w1 <= w2 for w1, w2 in zip(words, words[1:])))
