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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int len = preorder.length;
        HashMap<Integer, Integer> inorderIndex = new HashMap<Integer,Integer>();
        for(int i = 0; i < len; i++) inorderIndex.put(inorder[i],i);
        return buildTree(preorder,0,inorder,0,len-1, inorderIndex);
    }
    private TreeNode buildTree(int[] preorder, int preStart, int[] inorder,int inStart, int inEnd, HashMap<Integer, Integer> inorderIndex) {
        if(preStart == preorder.length) return null;
        int value = preorder[preStart];
        TreeNode t = new TreeNode(value);
        int j = inorderIndex.get(value);
        int leftSize = j-inStart;
        if(inStart == j) t.left = null;
        else t.left = buildTree(preorder,preStart+1, inorder,inStart,j-1,inorderIndex);
        if(j == inEnd) t.right = null;
        else t.right = buildTree(preorder,preStart+leftSize + 1, inorder, j+1, inEnd, inorderIndex);
        return t;
    }
}