/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int height = 0;
    int cnt = 0;
    public int countNodes(TreeNode root) {
        TreeNode t = root;
        while(t != null) {height++; t = t.left;}
        if(height <= 1) return height;
        cnt = (int) Math.pow(2, height - 1);//count all nodes except at the last level,plus the first node at the last level
        int n = (int) Math.pow(2, height - 1);
        int h = 1;
        while(root != null) {
            TreeNode l = root.left;
            int h1 = h; while(l != null) {h1++; l = l.right;}
            if(h1 != height) {root = root.left;}
            else {
                TreeNode r = root.right;
                int h2 = h; while(r != null) {h2++; r = r.left;}
                if(h2 != height) {cnt += n/2 - 1; return cnt;}
                else {cnt += n/2; root = root.right;}
            }
            n /= 2;
            h++;
        }
        return cnt;
    }
    
}