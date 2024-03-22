class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        //inspired by the top voted in discussion; The key idea is the speed of 2 pointers. The first do-while-loop ensures slow/fast pointers to be inside the circle, note that fast pointer is moving twice as fast as the slow pointer. The second while-loop comes from the fact that the 2 pointers must meet at the start of the loop, as can be verified by their starting and ending points. The fast and slow pointers in the second while loop moves with the same speed
        int slow = 0, fast = 0;
        do{
            slow = nums[slow];
            fast = nums[nums[fast]];
        }while(slow != fast);
        fast = 0;
        while(slow != fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};