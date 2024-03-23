class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int result = 0;
        unordered_map<int, int> sum_count;
        sum_count[0] = 1;
        for(int i = 0, sum = 0; i < nums.size(); i++){
            sum += nums[i];
            if(sum_count.find(sum - k) != sum_count.end()) result += sum_count[sum-k];
            sum_count[sum]++;
        }
        return result;
    }
};