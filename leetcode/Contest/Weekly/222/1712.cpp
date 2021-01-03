// 1712. Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        int n = nums.size();
        int M = 1e9+7;
        
        vector<int> prefix(n, 0);
        prefix[0] = nums[0];
        for (int i = 1; i < n; i++)
            prefix[i] = prefix[i-1] + nums[i];
        
        long long res = 0;
        for (int i = 0; i < n - 1; i++){
            int left = prefix[i];
            int remaining = prefix[n-1] - left;
            int max_mid = remaining / 2;
            
            int mid_start = lower_bound(prefix.begin()+i+1, prefix.end() - 1, left*2) - prefix.begin();
            int right_start = upper_bound(prefix.begin()+i+1, prefix.end() - 1, left + max_mid) - prefix.begin();
            
            res += max(0, right_start - mid_start);
            res %= M;
        }
        
        return res % M;
    }
};

// O(1) space
class Solution {
public:
    int waysToSplit(vector<int>& prefix) {
        int n = prefix.size();
        int M = 1e9+7;
        
        for (int i = 1; i < n; i++)
            prefix[i] += prefix[i-1];
        
        long long res = 0;
        for (int i = 0; i < n - 1; i++){
            int left = prefix[i];
            int remaining = prefix[n-1] - left;
            int max_mid = remaining / 2;
            
            int mid_start = lower_bound(prefix.begin()+i+1, prefix.end() - 1, left*2) - prefix.begin();
            int right_start = upper_bound(prefix.begin()+i+1, prefix.end() - 1, left + max_mid) - prefix.begin();
            
            res += max(0, right_start - mid_start);
            res %= M;
        }
        
        return res % M;
    }
};