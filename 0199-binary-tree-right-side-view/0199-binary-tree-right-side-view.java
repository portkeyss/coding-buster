/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//import java.util.LinkedList;
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new LinkedList<Integer>();
        LinkedList<TreeNode> queuePre = new LinkedList<TreeNode>();
        if(root == null) return result;
        queuePre.addLast(root);
        while(!queuePre.isEmpty()) {
            result.add(queuePre.peekFirst().val);
            LinkedList<TreeNode> queueCur = new LinkedList<TreeNode>();
            while(!queuePre.isEmpty()) {
                TreeNode node = queuePre.removeFirst();
                if(node.right != null) queueCur.addLast(node.right);
                if(node.left != null) queueCur.addLast(node.left);
            }
            queuePre = queueCur;
        }
        return result;
    }
}