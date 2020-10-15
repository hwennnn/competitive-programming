# 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int right = -1, res = 0;
        
        for (int i = 0; i < arr.size(); i++){
            right = max(right, arr[i]);
            res += right == i;
        }
        
        return res;
    }
};