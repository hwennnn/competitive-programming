# 2131. Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        res = 0
        done = set()
        hasMiddle = False
        
        for word, count in list(counter.items()):
            r = word[::-1]
            
            if r == word:
                res += 2 * count
                if count & 1:
                    hasMiddle = True
                    res -= 2
            elif word not in done and r in counter:
                c1, c2 = counter[word], counter[r]
                res += len(word) * min(c1, c2) * 2
                done.add(r)
        
        if hasMiddle:
            res += 2
        
        return res
        
