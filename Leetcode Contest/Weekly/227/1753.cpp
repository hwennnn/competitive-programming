// 1753. Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones

class Solution {
public:
    int maximumScore(int a, int b, int c) {
        if (a < b)
            return maximumScore(b, a, c);
        
        if (b < c)
            return maximumScore(a, c, b);
        
        return b == 0 ? 0 : 1 + maximumScore(a-1, b-1, c);
    }
};
