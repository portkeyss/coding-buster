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
    public int sumNumbers(TreeNode root) {
        if(root == null) return 0;
        return sumNumbers(root, 0);
    }
    private int sumNumbers(TreeNode root, int num) {
        if(root.left == null && root.right == null) 
            return 10 * num + root.val;
        if(root.left != null && root.right == null)
            return sumNumbers(root.left, 10 * num + root.val);
        if(root.left == null && root.right != null)
            return sumNumbers(root.right, 10 * num + root.val);
        else
            return sumNumbers(root.left, 10 * num + root.val) + sumNumbers(root.right, 10 * num + root.val);
    }
}