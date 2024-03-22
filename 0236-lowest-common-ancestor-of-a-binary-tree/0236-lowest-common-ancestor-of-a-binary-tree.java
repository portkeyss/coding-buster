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
    TreeNode firstNode = null;
    TreeNode secondNode = null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(contains(p,q)) return p;
        if(contains(q,p)) return q;
        return lca(root, p, q);
    }
    private TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return null;
        if(p == root) {firstNode = p; secondNode = q; return null;}
        if(q == root) {firstNode = q; secondNode = p; return null;}
        TreeNode l = lca(root.left, p, q);
        if(l != null) return l;
        else if(firstNode != null) {
            if(contains(root.right, secondNode)) return root;
            else return null;
        }
        else return lca(root.right, p, q);
    }
    private boolean contains(TreeNode root, TreeNode p) {
        if(root == null) return false;
        if(root == p) return true;
        return contains(root.left, p) || contains(root.right, p);
    }
}