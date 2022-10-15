# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        N, M = len(players), len(trainers)
        players.sort()
        trainers.sort()
        res = 0
        firstPlayer = players[0]
        j = bisect_left(trainers, firstPlayer)
        
        if j == M: return 0
        
        for player in players:
            while j < M and player > trainers[j]:
                j += 1
                
            if j == M: break
                
            if player <= trainers[j]:
                res += 1
                j += 1
​
        return res
