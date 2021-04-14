# 86. Partition List
# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        front = cFront = ListNode(-1)
        back = cBack = ListNode(-1)
        curr = head
        
        while curr:
            v = curr.val
            if v < x:
                front.next = ListNode(v)
                front = front.next
            else:
                back.next = ListNode(v)
                back = back.next
            
            curr = curr.next
        
        res = cFront
        while cFront.next:
            cFront = cFront.next
            
        cFront.next = cBack.next
        
        return res.next
