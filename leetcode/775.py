# 775. Global and Local Inversions
# https://leetcode.com/problems/global-and-local-inversions/

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - v) <= 1 for i, v in enumerate(A))
​
