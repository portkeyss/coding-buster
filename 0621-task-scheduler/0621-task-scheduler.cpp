class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        /*This problem is to find the most tightly packed intervals. we may do this by contructing such interval. Inspired by approach 3 in solution, we use a grid to decribe the approach. Note that each time we fill in a series of same task, e.g. HHHHH, we do this by fill it starting from the leftmost slot, and move it downward. if it hits the bottom wall, we start from the top element of next leftmost column, and proceed downward. There is no need to worry about any short of cooling time. because the task occurances are sorted already, and the length of a specific task must be smaller or equal to the first task. If equal, there is no such worry about turning to next column. if less, either it ends before hitting the bottom in a single column, or, the last task in the next column would be at seperated by one bin(row), leaving enough cooling time. If the bins capacity runs out of space, we may still use the same way to append tasks to the bins as if we are expanding the bin. Of course, in this case, since no idle spot exists, total interval is simply the length of the orginal task sequence, i.e., no need to worry about bin sizes*/
        vector<int> map(26);
        for(char task: tasks){
            map[task-'A']++;
        }
        sort(map.begin(), map.end(), greater<int>());
        int tasks_len = tasks.size();
        int max = map[0];
        if(max == 0) return 0;
        int top_frequent_tasks = 0;
        for(int i = 0; i < map.size() && map[i] == max; i++) {
            top_frequent_tasks++;
        }
        int total_bin_capacity = (n + 1) * (max - 1) + top_frequent_tasks;
        return std::max(total_bin_capacity, tasks_len);
    }
};