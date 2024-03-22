public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int height = triangle.size();
        if (height == 1 ) return triangle.get(0).get(0);
        int[] sum = new int[height];
        for(int i = 0; i < height; i ++) sum[i] = triangle.get(height - 1).get(i);
        for(int i = height-2; i >=0; i --)
            for(int j = 0; j < triangle.get(i).size(); j ++)
               sum [j] = triangle.get(i).get(j) + (sum[j] < sum[j+1] ? sum[j]:sum[j + 1]);
        return sum[0];
    }
}