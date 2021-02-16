# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        res = set()
        
        for i in range(1<<n):
            s = list(S)
            for j in range(n):
                if i >> j & 1:
                    s[j] = s[j].upper()
                else:
                    s[j] = s[j].lower()
​
            res.add("".join(s))
                
        return list(res)
