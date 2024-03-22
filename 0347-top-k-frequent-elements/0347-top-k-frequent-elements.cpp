#define p pair<int, int>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {         
        unordered_map<int, int> m;
        for(int i:nums) m[i]++;
        struct compare{
            bool operator()(const p& a, const p& b){
                return a.second > b.second;
            }
        };
        priority_queue<p, vector<p>, compare> pq;
        
        for(auto p1 : m){
            if(pq.size() < k) pq.push(p1);
            else if(pq.top().second < p1.second) {
                pq.pop();
                pq.push(p1);
            }
        }
        vector<int> result(k);
        int i = 0;
        while(!pq.empty()){  
            result[i++]=pq.top().first;
            pq.pop();
        }
        return result;
    } 
};