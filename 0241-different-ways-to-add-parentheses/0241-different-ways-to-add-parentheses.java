public class Solution {
    HashMap<Integer, HashMap<Integer, ArrayList<Integer>>> aux = new HashMap<Integer, HashMap<Integer, ArrayList<Integer>>>();
    public List<Integer> diffWaysToCompute(String input) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        ArrayList<Character> operators = new ArrayList<Character>();
        for(int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if(ch == '*' || ch == '+' || ch =='-') {
                operators.add(ch);
            } else {
                int num = 0;
                while(i < input.length() && input.charAt(i) >= '0' && input.charAt(i) <= '9') {
                    num = 10 * num + input.charAt(i) - '0'; i++;
                }
                nums.add(num);
                i--;
            }
        }
        return diffWaysToCompute(nums, operators, 0, nums.size() - 1);
    }
    private List<Integer> diffWaysToCompute(ArrayList<Integer> nums, ArrayList<Character> operators, int start, int end) {
        if(aux.get(start) != null && aux.get(start).get(end) != null) return aux.get(start).get(end);
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(start == end) {
            list.add(nums.get(start)); return list;
        }
        for(int i = start; i < end; i++) {
            char operator = operators.get(i);
            List<Integer> left = diffWaysToCompute(nums, operators, start, i);
            List<Integer> right = diffWaysToCompute(nums, operators, i + 1, end);
            for(int j : left) {
                for(int k: right) {
                    if(operator == '*') list.add(j * k);
                    else if(operator == '+') list.add(j + k);
                    else list.add(j - k);
                }
            }
        }
        if(aux.get(start) != null) aux.get(start).put(end, list);
        else {
            HashMap<Integer, ArrayList<Integer>> hm = new HashMap<Integer, ArrayList<Integer>>();
            hm.put(end, list);
            aux.put(start, hm);
        }
        return list;
    }
}