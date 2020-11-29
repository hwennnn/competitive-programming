// 1669. Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *p = list1;
        for (int i = 0; i < a - 1; i++)
            p = p->next;
        
        ListNode *q = list1;
        for (int i = 0; i <= b; i++)
            q = q->next;
        
        ListNode *curr = list2;
        while (curr->next)
            curr = curr->next;
        
        curr->next = q;
        p->next = list2;
        
        return list1;
    }
};