// 713. Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int c = 1, res = 0;
        
        for (int i = 0,j = 0; j < nums.size(); j++){
            c *= nums[j];
            while (i <= j && c >= k)
                c /= nums[i++];
            res += (j - i + 1);
        }
        
        return res;
    }
};