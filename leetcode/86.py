# 86. Partition List
# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        A, front, back = [], [], []
        curr = head
​
        while curr:
            A.append(curr.val)
            curr = curr.next
        
        for num in A:
            if num >= x:
                back.append(num)
            else:
                front.append(num)
​
        res = dummy = ListNode(-1)
        
        for num in front + back:
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next
