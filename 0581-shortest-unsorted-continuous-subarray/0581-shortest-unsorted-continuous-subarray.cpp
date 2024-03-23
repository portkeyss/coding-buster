class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        int i = 0, j = nums.size() - 1;
        while(i <= j && nums[i] == sorted_nums[i]) i++;
        while(i <= j && nums[j] == sorted_nums[j]) j--;
        return j - i + 1;
    }
};