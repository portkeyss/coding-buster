/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private int diameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        depthOfBinaryTree(root);
        return diameter;
    }
    private int depthOfBinaryTree(TreeNode root){
        if(root == null) return 0;
        int leftDepth = depthOfBinaryTree(root.left);
        int rightDepth = depthOfBinaryTree(root.right);
        diameter = Math.max(diameter,leftDepth + rightDepth);
        return 1 + Math.max(leftDepth, rightDepth);
    }
}