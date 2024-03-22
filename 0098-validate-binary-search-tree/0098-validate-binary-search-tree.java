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
    public boolean isValidBST(TreeNode root) {
        //inorder traversal naturally follows the sequence
        if(root == null) return true;
        List<Integer> l = new LinkedList<Integer>();
        return isValidBST(root, l);
    }
    private boolean isValidBST(TreeNode root, List<Integer> l) {
        if(root.left != null && !isValidBST(root.left,l)) return false;
        if(!l.isEmpty()) {
            if(l.get(0) >= root.val) return false;
            l.remove(0);
        }
        l.add(root.val);
        if(root.right != null && !isValidBST(root.right, l)) return false;
        return true;
    }
}