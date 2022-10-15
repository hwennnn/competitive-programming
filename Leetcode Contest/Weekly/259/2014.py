# 2014. Longest Subsequence Repeated k Times
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        def isSubsequence(s, t):
            t = iter(t)
            
            return all(c in t for c in s)
        
        hot = "".join(key * (freq // k) for key, freq in collections.Counter(s).items())
​
        combs = set()
        for l in range(len(hot) + 1):
            for cand in combinations(hot, l):
                for perm in permutations(cand):
                    combs.add("".join(perm))
        
        combs = sorted(combs, key = lambda x: (len(x), x), reverse = 1)
        for comb in combs:
            if isSubsequence(comb * k, s):
                return comb
