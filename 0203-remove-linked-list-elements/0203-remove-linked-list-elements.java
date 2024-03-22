/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        while(head != null && head.val == val) head = head.next;
        ListNode pre = new ListNode(0);//initialized only for auxillary purpose, this initial value can take any value
        ListNode l = head; // l is the old list listNode cursor
        while(l != null) {
            if(l.val != val) {
                pre.next = l;//each step we find a valid node,we make the previous valid node's next point to cur node
                pre = l;
            }
            l = l.next;
        }
        pre.next = null;//This step is easily forgotten. be sure to notice that if the list ends with one or more nodes with values that equal to val, pre.next must be set to zero.
        return head;
    }
}