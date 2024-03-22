public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if(numerator == 0) return "0";
        boolean flag = (numerator < 0)^(denominator < 0);
        long Numerator = Math.abs((long)numerator);
        long Denominator = Math.abs((long)denominator);
        StringBuffer sb = new StringBuffer(); 
        if(flag) sb.append('-');
        sb.append(Numerator / Denominator);
        Numerator %= Denominator;
        if(Numerator == 0) return sb.toString(); 
        sb.append('.'); 
        HashMap<Long,Integer> hm = new HashMap<Long,Integer>();
        for(int i = sb.length(); Numerator != 0; i++) {
            if(hm.containsKey(Numerator)) break;
            hm.put(Numerator,i);
            Numerator *= 10;
            sb.append(Numerator/Denominator);
            Numerator %= Denominator;
        }
        if(Numerator == 0) return sb.toString(); 
        int i = hm.get(Numerator);
        sb = sb.insert(i,'(');
        sb.append(')');
        return sb.toString();
    }
}