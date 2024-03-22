/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        ListNode p = head;
        int length = 1;
        while (p.next != null){
            length ++;
            p= p.next;
        }
        
        return sortedListToBST (head, length);
    }
    
    private TreeNode sortedListToBST(ListNode head, int length) {
        if (length == 0) return null;
        if (length <= 1) return new TreeNode(head.val);
        
        ListNode p=head;
        int count = 1;
        while (count <= length/2) {
            count ++;
            p = p.next;
        }
        TreeNode t = new TreeNode (p.val);
        t.left = sortedListToBST(head, length/2);
        t.right = sortedListToBST(p.next, length -1 -length/2);
        return t;
    }
    
    
}