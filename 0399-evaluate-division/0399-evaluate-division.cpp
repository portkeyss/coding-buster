class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        //inspired by top voted "9 lines "Floyd\u2013Warshall" in Python" in discussion, an variation of Floyd–Warshall
        unordered_map<string, unordered_map<string, double>> dist;
        for(int i = 0; i < equations.size(); i++){
            vector<string> equation = equations[i];
            dist[equation[0]][equation[1]] = values[i];
            dist[equation[1]][equation[0]] = 1/values[i];
            dist[equation[0]][equation[0]] = 1;
            dist[equation[1]][equation[1]] = 1;
        }
        for(auto& k: dist){
            for(auto& i: k.second){
                for(auto& j: k.second){
                     dist[i.first][j.first] = dist[i.first][k.first] * dist[k.first][j.first];
                }      
            }
        }
        vector<double> result;
        for(vector<string>& query: queries){
            result.push_back(dist.count(query[0]) && dist[query[0]].count(query[1]) ? dist[query[0]][query[1]]:-1.0);
        }       
        return result;
    }
};