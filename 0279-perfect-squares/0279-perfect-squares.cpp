class Solution {
public:
    int numSquares(int n) {
        vector<int> nums(n+1,n);
        nums[0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j * j <= i; j++) {
                nums[i] = min(1 + nums[i - j * j], nums[i]);
            }
        }
        return nums[n];
    }
};