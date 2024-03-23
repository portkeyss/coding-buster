class Solution {
public:
    string decodeString(string s) {
        string result;
        
        stack<int> ks;
        stack<string> str_stk;
        
        int cnt  = 0;
        
        for(int i = 0; i < s.length(); i++){
            if(s[i]>= '0' && s[i] <= '9'){
                cnt = 10 * cnt + (s[i] - '0');
            }else if(s[i] == '[') {
                ks.push(cnt);
                str_stk.push("");
                cnt = 0;
            }else if(s[i] == ']') {
                string str = str_stk.top();
                str_stk.pop();
                
                string& str_cur_level = str_stk.empty()? result: str_stk.top();
                for(int j = 0; j < ks.top(); j++) str_cur_level += str;
                ks.pop();
            }else{
                string& str_cur_level = str_stk.empty()? result: str_stk.top();
                str_cur_level += s[i];    
            }
        }
        return result;
    }
};