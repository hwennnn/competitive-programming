// 102. Binary Tree Level Order Traversal
// https://leetcode.com/problems/binary-tree-level-order-traversal/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    // using deque
    vector<vector<int>> levelOrder(TreeNode* root) {
        deque<TreeNode*> deq = {root};
        vector<vector<int>> res;
        
        if (root == nullptr) return res;
        
        while (deq.size() > 0){
            vector<int> tmp;
            int length = deq.size();
            
            while (length--){
                TreeNode* node = deq.front();
                tmp.push_back(node->val);
                deq.pop_front();
                
                if (node->left){
                    deq.push_back(node->left);
                }
                
                if (node->right){
                    deq.push_back(node->right);
                }
            }
            
            res.push_back(tmp);
        }
        
        return res;
    }

    // using queue
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q; q.push(root);
        vector<vector<int>> res;
        
        if (root == nullptr) return res;
        
        while (q.size() > 0){
            vector<int> tmp;
            int length = q.size();
            
            while (length--){
                TreeNode* node = q.front();
                tmp.push_back(node->val);
                q.pop();
                
                if (node->left){
                    q.push(node->left);
                }
                
                if (node->right){
                    q.push(node->right);
                }
            }
            
            res.push_back(tmp);
        }
        
        return res;
    }
};