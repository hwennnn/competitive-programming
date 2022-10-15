# 2131. Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter()
        res = leftover = 0
        
        for word in words:
            if word[0] == word[1]:
                if counter[word] > 0:
                    leftover -= 1
                    res += 4
                    counter[word] -= 1
                else:
                    leftover += 1
                    counter[word] += 1
            else:
                if counter[word[::-1]] > 0:
                    res += 4
                    counter[word[::-1]] -= 1
                else:
                    counter[word] += 1
        
        if leftover > 0:
            res += 2
        
        return res
                    
