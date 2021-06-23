# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        
        while head:
            nxt = head.next
            head.next = res
            res = head
            head = nxt
        
        return res
