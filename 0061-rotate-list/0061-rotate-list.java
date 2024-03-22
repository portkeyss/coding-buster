/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int n) {
      
        if  ( head == null) return head;
        int length = 0;
        ListNode q = head;
        while(q != null){
            q = q.next;
            length ++;
        }
        
        //count how much steps the head pointer should shift towards right
        int rot = (length -n % length) % length;
        
        if (rot == 0 ) return head;
        
        ListNode p = head;
        int k = 0;
        while (k < rot -1 ){
            p = p.next;
            k++;
        }

        ListNode h = p.next;
        p.next = null;
        
        p = h;
        while (p.next != null){
            p = p.next;
            
        }
        p.next = head;
        return h;
    }
}