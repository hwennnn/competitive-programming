# 1686. Stone Game VI
# https://leetcode.com/problems/stone-game-vi/

class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        res = sorted(zip(A,B), key = sum)

        alice = sum(a for a,b in res[::-2])
        bob = sum(b for a,b in res[-2::-2])
        
        return 0 if alice == bob else 1 if alice > bob else -1
    