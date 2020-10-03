// 90. Subsets II
// https://leetcode.com/problems/subsets-ii/

// bitmasking
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

// check and skip when repeated
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            bool isRepeated = false;
            for (int j = 0; j < n; ++j)
                if (i >> j&1){
                    if (j > 0 && nums[j]==nums[j-1] && (i>>(j-1)&1) == 0){
                        isRepeated = true;
                        break;
                    }else{
                        c.push_back(nums[j]);
                    }
                }
                    
            if (!isRepeated){
                res.push_back(c);
            }
        }
        
        return res;
    }
};