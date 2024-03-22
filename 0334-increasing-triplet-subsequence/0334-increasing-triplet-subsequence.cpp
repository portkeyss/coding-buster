class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int min = INT_MAX;
        int mid = INT_MAX;
        for(int i: nums){
            if(i < min) min = i;
            else if(i > min){
                if(i < mid) mid = i;
                else if(i > mid) return true;
            }
        }
        return false;   
    }
};