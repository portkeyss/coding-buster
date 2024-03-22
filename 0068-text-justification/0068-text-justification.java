public class Solution {
    public List<String> fullJustify(String[] words, int L) {
        List<String> result = new ArrayList<String>(); 
        int start = 0, cur = 0; 
        while(start < words.length) { 
            StringBuffer sb = new StringBuffer(); 
            sb.append(words[cur]);  
            int len = words[cur].length(); cur++;  
            while(cur < words.length) { 
                len += 1 + words[cur].length(); 
                if(len > L) break;
                else cur++;
            } 
            if(cur == words.length) { 
                for(int i = start + 1; i < cur; i++) sb.append(' ').append(words[i]); 
                while(sb.length() < L) sb.append(' '); 
                result.add(sb.toString()); 
                break; 
            } 
            if(cur == start + 1) { 
                while(sb.length() < L) sb.append(' '); 
                result.add(sb.toString()); 
                start = cur; 
                continue;
            } 
 
            int averageMoreSpaces = (L - len + words[cur].length() + 1) / (cur - start - 1); 
            int res_spaces = (L - len + words[cur].length() + 1) % (cur - start - 1);
            int temp1 =  (L - len + words[cur].length() + 1), temp2 = (cur - start - 1);
             
            StringBuffer rightSpacesBuffer = new StringBuffer(); 
            for(int k = 0; k < averageMoreSpaces; k++) rightSpacesBuffer.append(' '); 
            String rightSpace = rightSpacesBuffer.toString(); 
            String leftSpace = rightSpace + " "; 
            for(int i = start + 1; i < start + 1 + res_spaces; i++) { 
                sb.append(' ').append(leftSpace).append(words[i]); 
            } 
            for(int i = start + 1 + res_spaces; i < cur; i++) { 
                sb.append(' ').append(rightSpace).append(words[i]);
            } 
             
            result.add(sb.toString());
            start = cur ; 
        } 
        return result;
    }
}