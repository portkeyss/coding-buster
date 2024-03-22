/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {
    Deque<Integer> q = new LinkedList<Integer>();
    
    public BSTIterator(TreeNode root) {
       inorderTraverse(root);
    }
    private void inorderTraverse(TreeNode root) {
       if(root == null) return;
       inorderTraverse(root.left);
       q.add(root.val);
       inorderTraverse(root.right);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !q.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        return q.poll();
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */