class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res = nums;
        int n = nums.size();
        int mid = n%2 == 0? n/2-1 : n/2;
        for(int i = 0; i <= mid; i++) {
            res[2* (mid - i)] = nums[i];
        }
        for(int j = mid + 1; j < n; j++) {
            res[1 + 2 * (n - 1 -j)] = nums[j]; 
        }
        nums = res;
    }
};