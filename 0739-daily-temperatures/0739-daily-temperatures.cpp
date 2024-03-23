class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> result(T.size());
        stack<int> idx_stack;
        for(int i = T.size() - 1; i >= 0; i--){
            while(!idx_stack.empty() && T[i] >= T[idx_stack.top()]) idx_stack.pop();
            result[i] = idx_stack.empty() ? 0 : (idx_stack.top() - i);
            idx_stack.push(i);
        }
        return result;
    }
};