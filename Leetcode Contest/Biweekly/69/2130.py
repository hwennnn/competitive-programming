# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        A = []
        
        while head:
            A.append(head.val)
            head = head.next
        
        res = float('-inf')
        n = len(A)
        
        for i in range(n // 2):
            res = max(res, A[i] + A[n - 1 - i])
        
        return res
