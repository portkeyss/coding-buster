public class Solution {
    public int numTrees(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        int num = 2 * numTrees(n-1);
        for (int i = 1; i <= n -2 ; i ++)
           num = num + (numTrees(i) * numTrees(n-i-1));
        return num;
    }
}