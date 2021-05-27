# 318. Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def construct(word):
            A = [False] * 26
            
            for w in word:
                v = ord(w) - ord('a')
                A[v] = True
            
            return A
        
        def hasCommon(A, B):
            return any(a and b for a,b in zip(A,B))
        
        S = [construct(word) for word in words]
        n = len(S)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if not hasCommon(S[i], S[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res
