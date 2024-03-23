class Solution {
public:
    int longestSubstring(string s, int k) {   
        int longest = 0;
        for(int unique_char_target = 1; unique_char_target <= 26; unique_char_target++){
            vector<int> freq(26);
            int start = 0, end = 0;
            int unique_char = 0;
            while(end < s.length()){
                if(freq[s[end++]-'a']++ == 0){
                    unique_char++;
                }
                while(unique_char > unique_char_target) {
                    if(freq[s[start++]-'a']-- == 1){
                        unique_char--;
                    }  
                }
                bool good_substring = true;
                for(int i = 0; i < 26; i++){
                    if(freq[i] > 0 && freq[i] < k){
                        good_substring = false;
                        break;
                    }
                }
                if(good_substring) longest = max(longest, end - start);
            }       
        }
        return longest;
    }
};