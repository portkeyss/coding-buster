public class Solution {
    public int findKthLargest(int[] nums, int k) {
        Heap hp = new Heap(nums.length);
        for(int i: nums) hp.push(i);//build the max-heap
        for(int i = 0; i < k - 1; i++) hp.pop();
        return hp.pop();
    }
    public static class Heap {
        int[] storage;
        int sz;
        public Heap(int capacity) {
            storage = new int[capacity];
            sz = 0;
        }
        public int pop() {
            swap(0,sz - 1);
            sz--;
            int i = 0;
            while(i < sz) {
                if(2 * i + 1 >= sz) break;
                else if(2 * i + 2 >= sz) {
                    if(storage[i] >= storage[2 * i + 1]) break;
                    else {swap(i,2 * i + 1); i = 2 * i + 1;}
                }
                else if (storage[i] >= storage[2 * i + 1] && storage[i] >= storage[2 * i + 2]) break;
                else {
                    if(storage[2 * i + 1] < storage[2 * i + 2]) {swap(i, 2 * i + 2); i = 2 * i + 2;}
                    else {swap(i, 2 * i + 1); i = 2 * i + 1;}
                }
            }
            return storage[sz];
        }
        public void push(int element) {
            storage[sz++] = element;
            int j = sz - 1;
            while(j > 0 && storage[j] > storage[(j - 1) / 2]) {
                swap(j, (j - 1) / 2);
                j = (j - 1) / 2;
            }
        }
        public void swap(int i, int j) {
            int temp = storage[i];
            storage[i] = storage[j];
            storage[j] = temp;
        }
    }
}