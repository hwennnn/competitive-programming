# 2037. Minimum Number of Moves to Seat Everyone
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        
        for seat, student in zip(seats, students):
            res += abs(seat - student)
        
        return res
