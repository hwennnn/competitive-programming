# 2335. Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)
