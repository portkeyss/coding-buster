class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int i = start;
        int n = distance.size();
        int dist_1 = 0;
        while(i != destination){
            dist_1 += distance[i];
            i = (i + 1) % n;
        }
        int dist_2 = 0;
        while(i != start){
            dist_2 += distance[i];
            i = (i + 1) % n;
        }
        return std::min(dist_1, dist_2);
    }
};