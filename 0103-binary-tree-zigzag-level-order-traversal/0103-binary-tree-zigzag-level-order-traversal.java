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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Stack<TreeNode> t1 = new Stack<TreeNode>();
       
        if(root == null) return result;
        t1.push(root);
        boolean order = true;
        while (!t1.isEmpty()) {
             Stack<TreeNode> t2 = new Stack<TreeNode>();
            List<Integer> l = new ArrayList<Integer>();
            while (!t1.isEmpty()) {
                TreeNode p1 = t1.pop();
                l.add(p1.val);
                if(order) {
                    if(p1.left != null) t2.push(p1.left);
                    if(p1.right != null) t2.push(p1.right);
                }
                else {
                    if(p1.right != null) t2.push(p1.right);
                    if(p1.left != null) t2.push(p1.left);
                }
            }
            result.add(l);
            t1 = t2;
            order = !order;
        }
        return result;
    }
}