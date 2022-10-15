// 1250. Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
public:
    bool isGoodArray(vector<int>& A) {
        int res = A[0];
        for (int a: A)
            res = gcd(res, a);
        return res == 1;
    }
};