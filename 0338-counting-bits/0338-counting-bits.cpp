class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> result(1 + num);
        for(int i = 1; i <= num; i++){
            if(i&1) result[i] = result[i-1] + 1;//i is odd num,i.e., last bit is 1
            else result[i] = result[i >> 1]; //i is even num, i.e., last bit is 0
        }
        return result;
    }
};