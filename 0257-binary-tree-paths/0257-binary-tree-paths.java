/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    List<String> result;
    public List<String> binaryTreePaths(TreeNode root) {  
        result = new LinkedList<String>();
        if(root == null) return result;
        traverseTree(root, "");
        return result;
    }
    private void traverseTree(TreeNode root, String path){
        path += root.val;//note that path is a now a new object(string is immutable, any new concatenated string is new instance)
        if(root.left == null && root.right == null){       
            result.add(path);       
        }else{
            path += "->";
            if(root.left != null){        
                traverseTree(root.left, path);
            }
            if(root.right != null){
                traverseTree(root.right, path);
            }
        }
        return;
    }
}