# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int):
        res = []
        
        ans = head
        while head:
            res.append(head)
            head = head.next
            
        n = len(res)
        if n - k - 1 < 0: return ans.next
        
        res[n-k-1].next = res[n-k+1] if (n-k+1) < n else None

        return ans
            