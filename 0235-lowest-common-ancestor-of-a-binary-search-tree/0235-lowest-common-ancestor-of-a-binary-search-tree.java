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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p.val > q.val) return lowestCommonAncestor(root, q, p);
        TreeNode t = root;
        while(t != null) {
            if(t.val > q.val) t = t.left; 
            else if(p.val > t.val) t = t.right;
            else return t;
        }
        return null;
    }
}