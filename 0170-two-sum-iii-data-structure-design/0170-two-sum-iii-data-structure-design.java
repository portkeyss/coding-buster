public class TwoSum {
    HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
	public void add(int number) {
	    if(!hm.containsKey(number)) hm.put(number,1);
	    else hm.put(number,hm.get(number)+1);
	}

	public boolean find(int value) {
	    if(value % 2 == 0 && hm.containsKey(value/2) && hm.get(value/2) >= 2) return true;
	    for(Integer i: hm.keySet()) {
	        if(2 * i == value) continue;//this line is easily forgotten, but it is useful because equal cases has been treated before the loop, and if we can reach this ,it means no equal value exists and we must move to next integer in hm rather than let it do a contain search
	        if(hm.containsKey(value - i)) return true;
	    }
	    return false;
	}
}