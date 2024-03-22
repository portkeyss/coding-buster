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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> l = new LinkedList<List<Integer>>();
        
        if(root == null) return l;
        
        LinkedList<TreeNode> s = new LinkedList<TreeNode>();
        s.add(root);
        
        while(!s.isEmpty()) {
            LinkedList<TreeNode> t = new LinkedList<TreeNode>();
            List<Integer> p = new LinkedList<Integer>();
            while(!s.isEmpty()) {
                TreeNode treeNode = s.poll();
                p.add(treeNode.val);
                if(treeNode.left != null) t.add(treeNode.left);
                if(treeNode.right != null) t.add(treeNode.right);
            }
            l.add(p);
            if(!t.isEmpty()) s = t;
        }
        return l;
    }
}