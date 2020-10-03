// 90. Subsets II
// https://leetcode.com/problems/subsets-ii/

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        set<vector<int>> s;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            for (int j = 0; j < n; ++j)
                if (i >> j&1)
                    c.push_back(nums[j]);
            
            if (s.find(c) == s.end()){
                s.insert(c);
                res.push_back(c);
            }
                
        }
        
        return res;
    }
};