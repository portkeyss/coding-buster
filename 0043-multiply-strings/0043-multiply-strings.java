public class Solution {
    public String multiply(String num1, String num2) {
        if(num1.equals("0") || num2.equals("0") ) return "0";
        ArrayList<Integer> p = new ArrayList<Integer>();
        int end1 = num1.length() - 1;
        int end2 = num2.length() - 1;
        while( num1.charAt(end1) == 0) {end1--; p.add(0);}
        while( num2.charAt(end2) == 0) {end2--; p.add(0);}
        String s1 = num1;
        String s2 = num2;
        if(end1 < end2) {s1 = num2; s2 = num1; int temp = end1; end1 = end2; end2 = temp;}
        
        
        int i2 = end2;
        while(i2 > -1) {
            int carry = 0;
            int i1 = end1; 
            while(i1 > -1) {
                int n;
                int cur = end2 - i2 + end1 - i1;
                if(cur < p.size()) 
                    {n =(s1.charAt(i1) - '0') * (s2.charAt(i2) - '0') + carry + p.get(cur); p.set(cur, n % 10);}
                else {n = (s1.charAt(i1) - '0') * (s2.charAt(i2) - '0') + carry; p.add( n % 10);}

                carry = n / 10;
                i1--;
            }
            if(carry != 0) p.add(carry);
            i2--;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0 ; i < p.size(); i++) 
            sb.append(p.get(i));
        return sb.reverse().toString();
    }
}