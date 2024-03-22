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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<Integer>();
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        if(root == null) return result;
        stack.addLast(root);
        while(!stack.isEmpty()) {
            TreeNode cur = stack.removeLast();
            result.add(cur.val);
            if(cur.right != null) stack.addLast(cur.right);
            if(cur.left != null) stack.addLast(cur.left);
        }
        return result;
    }
}