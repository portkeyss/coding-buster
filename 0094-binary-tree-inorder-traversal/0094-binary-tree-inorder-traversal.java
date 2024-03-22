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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<Integer>();
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        if(root == null) return result;
        stack.addLast(root);
        TreeNode lastNode = null;
        while(!stack.isEmpty()) {
            TreeNode cur = stack.peekLast();
            if(cur.left != null && (lastNode == null || lastNode.left == cur || lastNode.right == cur)) {
                stack.addLast(cur.left);
            }
            else {
                stack.removeLast(); result.add(cur.val);
                if(cur.right != null) stack.addLast(cur.right);
            }
            lastNode = cur;
        }
        return result;
    }
}