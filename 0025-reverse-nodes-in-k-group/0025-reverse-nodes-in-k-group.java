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
    public ListNode reverseKGroup(ListNode head, int k) {
        
        if (k < 2 || head == null) return head;
        
        ListNode pre = null;
        ListNode cur = head;
        ListNode post = head;
        
        ListNode s = null;
        ListNode p = null;// the old starting position of the previous block
        
        int length = 1;
        while(cur.next != null) {
        length++;
        cur = cur.next;
        }
        
        if(k > length) return head;
        
        cur = head;

        int count = 1;
        while(count <= length - length % k){
              p = s;
              s = post;
              if(post!= null){
                 pre = cur;
                 cur = cur.next;
                 count ++;
              }
              while((count - 1) % k !=0){
                   post = cur.next;
                   cur.next = pre;
                   pre = cur;
                   cur = post;
                   count ++;
              }
              
              if(p == null) head = pre;
              else p.next = pre;//the old start position of the previous block must preceed the old end position of new block               
        }
        s.next = post;
        return head;
    }
}