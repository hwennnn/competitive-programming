# 1700. Number of Students Unable to Eat Lunch
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = collections.deque(students)
        
        for s in sandwiches:
            if s in q:
                while q[0] != s:
                    q.append(q.popleft())
                
                q.popleft()
                
            else:
                return len(q)
        
        return 0