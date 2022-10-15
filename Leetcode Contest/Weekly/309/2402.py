# 2402. Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        usedCount = [0] * n
        h = []
        freshRooms = []
​
        for roomId in range(n):
            heappush(freshRooms, (0, roomId))
        
        for start, end in meetings:
            temp = []
            
            while h and h[0][0] < start:
                endTime, roomId = heappop(h)
                temp.append((start, roomId))
            
            for endTime, roomId in temp:
                heappush(h, (endTime, roomId))
            
            duration = end - start
​
            if not h or (freshRooms and h and h[0][0] > start):
                endTime, roomId = heappop(freshRooms)
            else:
                endTime, roomId = heappop(h)
                
            usedCount[roomId] += 1
            d = endTime + duration if endTime != 0 else end
            heappush(h, (d, roomId))
​
        maxUsed = max(usedCount)
        
        for roomId, count in enumerate(usedCount):
            if count == maxUsed:
                return roomId
        
        return -1
