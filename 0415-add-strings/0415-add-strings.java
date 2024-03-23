class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sumString = new StringBuilder();
        if(num1.length() > num2.length()) {
            String tmp = num1;
            num1 = num2;
            num2 = tmp;
        }
        int pre = 0;
        for(int i = 1; i <= num1.length(); i++){
            int n1 = Character.getNumericValue(num1.charAt(num1.length() - i));
            int n2 = Character.getNumericValue(num2.charAt(num2.length() - i));
            int n3 = n1 + n2 + pre;
            sumString.append(n3 % 10);
            pre = n3 /10;
        }
        for(int i = num1.length() + 1; i <= num2.length(); i++) {
            int n2 = Character.getNumericValue(num2.charAt(num2.length() - i));
            int n3 = n2 + pre;
            sumString.append(n3 % 10);
            pre = n3 /10;
        }
        if(pre == 1) sumString.append(1);
        return sumString.reverse().toString();
    }
}