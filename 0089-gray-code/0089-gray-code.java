public class Solution {
    public List<Integer> grayCode(int n) {
       List<Integer> result = new ArrayList<Integer>();
       result.add(0);
       if(n == 0) return result;
       result.add(1);
       for(int sz = 2; sz < 1 << n; sz *= 2) {
           for(int j = sz-1; j >= 0; j--){
               result.add(sz+result.get(j));
           }
       }
       return result;
    }
}