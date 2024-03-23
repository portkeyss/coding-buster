class Solution {
public:
    bool canPartition(vector<int>& nums) {
        if(nums.size() < 2) return false;
        int s = 0;
        for(int num: nums) s += num;
        if(s % 2) return false;
        int half = s/2;
        vector<bool> sums(100 * 200 + 1, false);
        sums[0] = true;
        int max_sum = 0;
        for(int num: nums){       
            for(int j = max_sum; j >= 0; j--){//reverse iteration to avoid overlapping between current and previous steps; max_sum is the prviously reached largest idx and is updated after the finish of the current iteration, i.e. saving the time from brute force iteration from the largest idx in vector sums
                if(sums[j]) {
                    sums[j + num] = true;
                    if(j + num == half) return true;
                }
            }
            max_sum += num;
        }
        return false;
    }
};