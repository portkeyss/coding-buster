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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<Integer>();
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        if(root == null) return result;
        stack.addLast(root);
        TreeNode lastNode = null;
        while(!stack.isEmpty()) {
            TreeNode cur = stack.peekLast();
            if(cur.left == null && cur.right == null || lastNode != null && (lastNode == cur.left || lastNode == cur.right)) {
                stack.removeLast(); result.add(cur.val);
            }
            else {
                if(cur.right != null) stack.addLast(cur.right);
                if(cur.left != null) stack.addLast(cur.left);
            }
            lastNode = cur;
        }
        return result;
    }
}