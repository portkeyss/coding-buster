/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; left = null; right = null; }
 * }
 */
public class Solution {
    public List<TreeNode> generateTrees(int n) {
        List<TreeNode> treeList = new ArrayList<TreeNode>();
        if (n == 0) {
            treeList.add(null);
            return treeList;
        }
        if (n == 1) {
            treeList.add(new TreeNode(1));
            return treeList;
        }
        for (int i = 1; i <= n; i ++)
            for(TreeNode q1:generateTrees(i-1))
                for(TreeNode q2:generateTrees(n-i)){
                  TreeNode p = new TreeNode(i);
                  p.left = q1;
                  
                  p.right = shiftValue(q2, i);;
                  treeList.add(p);
                }
        return treeList;
    }
    /*private void shiftValue (TreeNode root, int s) {// It is still unclear why this method is not okay,maybe multiple call                                                          // changes the value of some nodes ?
        if (root == null) return;
        root.val = root.val + s;
        shiftValue(root.left, s);
        shiftValue(root.right, s);
    }*/
    private TreeNode shiftValue (TreeNode root, int s) {
        if (root == null) return null;
        TreeNode t = new TreeNode(root.val+s);
        t.left = shiftValue(root.left, s);
        t.right = shiftValue(root.right, s);
        return t;
    }
}