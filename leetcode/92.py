# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        
        dummy = ListNode(0)
        dummy.next = head

        c, prev = head, dummy
        for i in range(m-1):
            c = c.next
            prev = prev.next

        reverse = None
        for i in range(n-m+1):
            tmp = c
            c = c.next
            tmp.next = reverse
            reverse = tmp
        
        prev.next.next = c
        prev.next = reverse
        
        return dummy.next
        
        