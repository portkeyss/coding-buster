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
    public void flatten(TreeNode root) {
        if(root == null) return;
        LinkedList<TreeNode> t = new LinkedList<TreeNode>();
        enQue(root, t);
        TreeNode p = null, q = null;
        p = t.get(0);
        t.remove(0);
        while(!t.isEmpty()) {
            p.left = null;
            q = t.get(0);
            p.right = q;
            t.remove(0);
            p = q;
        }
    }
    private void enQue(TreeNode root, LinkedList<TreeNode> t) {
        if (root == null) return;
        t.add(root);
        enQue(root.left, t);
        enQue(root.right, t);
    }
}