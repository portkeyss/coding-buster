class Solution {
public:
    Solution(vector<int>& nums) {
        original = nums;
        array = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        array = original;
        return array;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int len = array.size();
        for(int i = 0; i < len; i++){
            int j = i + rand() % (len-i);
            swap(array[i], array[j]);
        }
        return array;
    }
private:
    vector<int> original;
    vector<int> array;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */