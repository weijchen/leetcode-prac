/*
Author: Jimmy Chen
PN: leetcode 461, Created Nov. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/hamming-distance/description/
Tag: Bit Manipulation
*/
// --------------------------------------------------- solution
/*
    n = n&(n-1) will always eliminate the least 1's in binary expression
*/
class Solution {
public:
    int hammingDistance(int x, int y) {
        int temp = x^y;
        int count = 0;
        while (temp!=0)
        {
          temp = temp&(temp-1);
          count++;
        }
        return count;
    }
};