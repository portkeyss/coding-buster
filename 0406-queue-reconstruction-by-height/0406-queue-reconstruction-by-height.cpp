class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        //inspired by the most voted  post in the disuccussion forum "Easy concept with Python/C++/Java Solution"
        vector<vector<int>> result;
        sort(people.begin(), people.end(), [](vector<int> a, vector<int> b){
            if(a[0] != b[0]) return a[0] > b[0];
            else return a[1] < b[1];
        });
        for(vector<int>& person: people){//The insertion ensures tight buildup until completion, i.e., no "holes" during the constructing process; The key idea is that the heights of ALL people in the existing list are all >= the person to be inserted in every step, therefore the insertion point is exactly the k value of this person
            result.insert(result.begin() + person[1], person);
        }
        return result;
    }
};