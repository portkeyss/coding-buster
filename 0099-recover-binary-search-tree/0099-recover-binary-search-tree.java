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
    public void recoverTree(TreeNode root) {
        TreeNode[] wrongNodes = new TreeNode[2];
        wrongNodes[0] = null; wrongNodes[1] = null;
        TreeNode[] previousNodes = new TreeNode[2];
        previousNodes[0] = null; previousNodes[1] = null;
        inorder(root, wrongNodes, previousNodes);//find first misplaced node, traverse from left to right, once found, return
        inorderReverse(root, wrongNodes, previousNodes);//find second misplaced node, traversing from right to left
        int temp = wrongNodes[0].val; wrongNodes[0].val = wrongNodes[1].val; wrongNodes[1].val = temp; //swap nodes
    }
    private void inorder(TreeNode root, TreeNode[] wrongNodes, TreeNode[] previousNodes) {
        if(wrongNodes[0] != null) return;
        
        if(root.left != null) inorder(root.left, wrongNodes, previousNodes);
        
        if(previousNodes[0] != null && previousNodes[0].val > root.val) {wrongNodes[0] = previousNodes[0]; return;}
        
        previousNodes[0] = root;
        if(root.right == null) return;
        inorder(root.right, wrongNodes, previousNodes);
    }
    
     private void inorderReverse(TreeNode root, TreeNode[] wrongNodes, TreeNode[] previousNodes) {
        if(wrongNodes[1] != null) return;
        
        if(root.right != null) inorderReverse(root.right, wrongNodes, previousNodes);
        
        if(previousNodes[1] != null && previousNodes[1].val < root.val) {wrongNodes[1] = previousNodes[1]; return;}
        
        previousNodes[1] = root;
        if(root.left == null) return;
        inorderReverse(root.left, wrongNodes, previousNodes);
    }
}