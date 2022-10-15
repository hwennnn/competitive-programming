# 1812. Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a, b = ord(coordinates[0]) - ord('a'), int(coordinates[1])
        
        return (a % 2 == 0 and b % 2 == 0) or (a & 1 and b & 1)
