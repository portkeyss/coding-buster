class Solution {
public:
    int firstUniqChar(string s) {
        int arr[26]={0};
        for(char c:s){
            arr[c - 'a']++;
        }
        for(int i=0; i < s.length(); i++){
            if(arr[s.at(i) - 'a']==1) return i;
        }
        return -1;
    }
};