# 908. Smallest Range I
# https://leetcode.com/problems/smallest-range-i/

# My Editorial: https://leetcode.com/problems/smallest-range-i/discuss/981882/Explanation-from-a-beginner%27s-perspective

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)
    




        