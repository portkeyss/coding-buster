public class Solution {
    public List<List<String>> partition(String s) {
        int len = s.length();
        List<List<List<String>>> resultList = new ArrayList<List<List<String>>>();
        List<List<String>> result = new ArrayList<List<String>>();
        List<String> l = new ArrayList<String>();
        l.add(s.substring(0,1)); result.add(l); resultList.add(result);
        for(int i = 1; i < len; i++) {
            result = new ArrayList<List<String>>();
            for(int j = 1; j <= i; j++) {
                if(!isPalindrome(s, j, i)) continue;
                List<List<String>> processed = resultList.get(j-1);
                for(List<String> lstr:processed) {
                    l = new ArrayList<String>();
                    for(String st:lstr) {
                        l.add(st);
                    }
                    l.add(s.substring(j,i+1));
                    result.add(l);
                }
            }
            if(isPalindrome(s, 0, i)) {l= new ArrayList<String>(); l.add(s.substring(0,i+1)); result.add(l);}
            resultList.add(result);
        }
        return result;
    }
    private boolean isPalindrome(String s, int l, int r) {
        while(l <= r && s.charAt(l) == s.charAt(r)) {l++; r--;}
        if(l > r) return true;
        return false;
    }
}