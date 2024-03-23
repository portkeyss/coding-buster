class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> sum_ab;
        unordered_map<int, int> sum_cd;
        for(auto a: A)
            for(auto b:B)
                sum_ab[a+b]++;
        int count = 0;
        for(auto c: C)
            for(auto d:D){
                auto it = sum_ab.find(-c-d);
                if(it!=sum_ab.end()) count += it->second;
            }              
        return count;
    }
};