# 1823. Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        A = [i for i in range(1, n + 1)]
        
        curr = 0
        
        while len(A) > 1:
            remove = A[(curr + k - 1) % len(A)]
            curr = (curr + k - 1) % len(A)
            A = [x for x in A if x != remove]
        
        return A[0]
