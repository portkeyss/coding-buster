class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        if(abs(S) > nums.size() * 1000) return 0;
        vector<int> sum_counts = construct_sums(nums, nums.size() - 1);
        return sum_counts[S + nums.size() * 1000];
    }
private:
    vector<int> construct_sums(vector<int>& nums, int i){  
        if(i == 0) {
            vector<int> cur_sum_counts(2001);
            cur_sum_counts[nums[i] + 1000]++;
            cur_sum_counts[-nums[i] + 1000]++;
            return cur_sum_counts;
        }
        vector<int> cur_sum_counts(2000 * (i + 1) + 1);
        vector<int> prev_sum_counts = construct_sums(nums, i - 1);
        for(int j = -1000 * i; j <= 1000 * i; j++) {
            if(prev_sum_counts[j + 1000 * i]) {
                cur_sum_counts[j + nums[i] + 1000 * (i+1)] += prev_sum_counts[j + 1000 * i];
                cur_sum_counts[j - nums[i] + 1000 * (i+1)] += prev_sum_counts[j + 1000 * i];
            }
        }
        return cur_sum_counts;
    }
};