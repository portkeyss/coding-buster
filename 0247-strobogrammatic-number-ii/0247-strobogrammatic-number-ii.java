class Solution {
    public List<String> findStrobogrammatic(int n) {
        return construct(n,n);
    }
    private List<String> construct(int p, int q){
        if(p == 0) return new ArrayList(Arrays.asList(""));
        if(p == 1) return new ArrayList(Arrays.asList("0","1","8"));
        
        List<String> list = construct(p - 2, q);
        
        List<String> result = new ArrayList<String>();
        for(String str: list){
            if(p != q) {
                result.add(0 + str + 0);
            }
             result.add(1 + str + 1);
             result.add(6 + str + 9);
             result.add(8 + str + 8);
             result.add(9 + str + 6);
        }
        return result;
        
    }
}