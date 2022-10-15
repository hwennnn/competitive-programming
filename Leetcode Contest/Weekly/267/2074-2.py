# 2074. Reverse Nodes in Even Length Groups
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        k = 1
        
        while curr:
            count = 0
            start = curr
            stack = []
            
            while curr and count < k:
                stack.append(curr.val)
                count += 1
                curr = curr.next
            
            if count % 2 == 0:
                while start != curr:
                    start.val = stack.pop()
                    start = start.next
            
            k += 1
        
        return head
