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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int len = inorder.length;
        HashMap<Integer, Integer> inorderIndex = new HashMap<Integer,Integer>();
        for(int i = 0; i < len; i++) inorderIndex.put(inorder[i],i);
        return buildTree(inorder,0,len-1,postorder,len-1, inorderIndex);
    }
     private TreeNode buildTree( int[] inorder,int inStart, int inEnd,int[] postorder, int postEnd, HashMap<Integer, Integer> inorderIndex) {
        if(postEnd == -1) return null;
        int value = postorder[postEnd];
        TreeNode t = new TreeNode(value);
        int j = inorderIndex.get(value);
        int rightSize = inEnd - j; 
        if(j == inEnd) t.right = null;
        else t.right = buildTree(inorder, j+1, inEnd, postorder, postEnd - 1, inorderIndex);
        if(inStart == j) t.left = null;
        else t.left = buildTree(inorder,inStart,j-1,postorder, postEnd - rightSize - 1, inorderIndex);
        return t;
    }
}