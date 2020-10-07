# 61. Rotate List
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next: return head
        
        curr = head
        l = 1
        
        while curr.next:
            curr = curr.next
            l += 1
        
        curr.next = head
        
        k = k % l
        
        for _ in range(l-k):
            curr = curr.next
        
        head = curr.next
        curr.next = None
        
        return head