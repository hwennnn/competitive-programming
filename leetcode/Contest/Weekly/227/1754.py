# 1754. Largest Merge Of Two Strings
# https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        deq1 = collections.deque(list(word1))
        deq2 = collections.deque(list(word2))
        
        res = []
        
        while deq1 and deq2:
            if "".join(list(deq1)) >= "".join(list(deq2)):
                res.append(deq1.popleft())
            else:
                res.append(deq2.popleft())
        
        leftover = list(deq1 or deq2)
        res += leftover
        
        return "".join(res)
