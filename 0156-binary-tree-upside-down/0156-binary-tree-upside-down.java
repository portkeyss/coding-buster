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
    public TreeNode upsideDownBinaryTree(TreeNode root) {
       LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
       while(root != null) {stack.addFirst(root); root = root.left;}
       TreeNode newRoot = stack.peekFirst();
       while(!stack.isEmpty()) {
           TreeNode t = stack.pollFirst();
           TreeNode p = stack.peekFirst();
           if(p != null) {t.left = p.right; t.right = p;}
           else {t.left = null; t.right = null;}
       }
       return newRoot;
    }
}