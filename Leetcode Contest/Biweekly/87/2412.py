# 2412. Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions

class Solution:
    def minimumMoney(self, A: List[List[int]]) -> int:
        return sum(max(0, i - j) for i, j in A) + max(map(min, A))
​
