public class Solution {
    public List<String> generateParenthesis(int n) {
        ArrayList<List<String>> storage = new ArrayList<List<String>>();
        List<String> result = new ArrayList<String>();
        List<String> list0 = new ArrayList<String>();
        list0.add("");storage.add(list0);
        for(int i = 1; i <= n; i++) {
            List<String> ls = new ArrayList<String>();
            for(int j = 0; j < i; j++) {
                for(String s: storage.get(j))
                    for(String ss: storage.get(i-1-j)) {
                        ls.add("(" + s + ")" + ss);
                    }
            }
            storage.add(ls);
        }
        return storage.get(n);
    }
}