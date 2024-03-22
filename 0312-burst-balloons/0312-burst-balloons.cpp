class Solution {
public:
    int maxCoins(vector<int>& nums) {
        //inspired by top voted post in forum "share some analysis and explanations".
        /*
        Basis idea:      
        1. small trick to avoid edge case. Just expand the array size by 2. padding With the leftmost and rightmost edge with 1's
        2. Working in time-reversed order, using divide and conquer and dynamical programming approach:
        Last bursted balloon always get award nums[-1]* nums[i]* nums[n], because nums[i] is the only balloon left; Then we think backward in time by reinstating nums[i]. We need to fill in all other slots. The total award should be the current award PLUS award earned in (left, i) and (i, right). The key to the divide and conquer approach is that the two intervals are not adjacent and they are independent.  Therefore, we do not need to worry about the sequence of "previous"(in time-reversed order) ballons burst. let dp[left][right] be the max award earned if the interval (left,right) are starting from empty. We recursively fills in the values top down, i.e., from (0, n) to the bottom case of (left, left + 1) which contains no ballons. 
        */
        vector<int> nums_aug(2 + nums.size());
        nums_aug[0] = 1;
        int n = 1;
        for(; n <= nums.size(); n++) nums_aug[n] = nums[n-1];
        nums_aug[n++] = 1;
        vector<vector<int>> dp(n,vector<int>(n));
        return dfs(nums_aug, dp, 0, n - 1);
    }
private:
    int dfs(vector<int>& nums, vector<vector<int>>& dp, int left, int right){
        if(left + 1 == right) return 0;
        if(dp[left][right] > 0) return dp[left][right];
        int award = 0; 
        for(int i = left + 1; i < right; i++){
            award = max(award, nums[left] * nums[i] * nums[right] + dfs(nums, dp, left, i) + dfs(nums, dp, i,right));
        }
        dp[left][right] = award;
        return award;
    }
};