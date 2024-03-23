class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> count(nums.size() + 1);
        for(int i : nums) count[i]++;
        vector<int> result;
        for(int j = 1; j <= nums.size(); j++){
            if(count[j] == 0) result.push_back(j);
        }
        return result;
    }
};