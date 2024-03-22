class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end(), greater<int>());
        if(coins.size() == 0) return amount == 0?0:-1;
        if(amount == 0) return 0;
        vector<int> count(amount+1);
        return coinChange(coins, amount, count);
    }
private:
    int coinChange(vector<int>& coins, int amount, vector<int>& count){
        if(amount < 0) return -1;
        if(amount == 0) return 0;
        if(count[amount]) return count[amount];
        int min_coin_num = INT_MAX;
        for(int coin: coins){
            int j = coinChange(coins, amount-coin, count);
            if(j != -1){
                min_coin_num =  min(min_coin_num, 1 + j);
            }
        }
        count[amount] = min_coin_num == INT_MAX? -1: min_coin_num;
        return count[amount];
    }
};