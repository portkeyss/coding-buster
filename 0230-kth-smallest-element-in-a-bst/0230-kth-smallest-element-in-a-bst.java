/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int cnt = 0;
    int res;
    public int kthSmallest(TreeNode root, int k) {
        count(root, k);
        return res;
    }
    private boolean count(TreeNode root, int k) {
        if(root == null) return false;
        if(count(root.left, k)) return true;
        cnt++;
        if(cnt == k) {res = root.val; return true;}
        return count(root.right, k);
    }
}