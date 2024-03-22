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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> l = new ArrayList<List<Integer>>();
        if(root == null) return l;
        List<Integer> currentPath = new ArrayList<Integer>();
        pathSum(root, sum, l,currentPath);
        return l;
    }
    private void pathSum(TreeNode root, int sum, List<List<Integer>> l, List<Integer> currentPath){
        currentPath.add(0,root.val);
        if(root.left == null && root.right == null && sum == root.val) {
                List<Integer> q = new ArrayList<Integer>();
                for(Integer p: currentPath) q.add(0,p);
                l.add(q);
        }
        if(root.left != null) pathSum(root.left, sum - root.val, l, currentPath);
        if(root.right != null) pathSum(root.right, sum - root.val, l, currentPath);
        currentPath.remove(0);
    }
}