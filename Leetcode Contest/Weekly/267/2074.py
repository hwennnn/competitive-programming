# 2074. Reverse Nodes in Even Length Groups
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(A, start, end):
            while start < end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            
            return A
        
        A = []
        curr = head
        length = 0
        
        while curr:
            A.append(curr.val)
            curr = curr.next
            length += 1
            
        index = count = 0
        k = 1
        while index < length:
            
            count += 1
            
            if k == count:
                if count % 2 == 0:
                    A = reverse(A, index - k + 1, index)
                    
                count = 0
                k += 1
            else:
                if index == length - 1 and count % 2 == 0:
                    A = reverse(A, index - count + 1, index)
            
            index += 1
        
        res = dummy = ListNode(-1)
        for v in A:
            dummy.next = ListNode(v)
            dummy = dummy.next
        
        return res.next
