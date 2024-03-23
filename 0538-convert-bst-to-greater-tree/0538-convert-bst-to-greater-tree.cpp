/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        if(root == nullptr) return nullptr;
        root->right = convertBST(root->right);
        root->val += right_sum;
        right_sum = root->val;
        root->left = convertBST(root->left);
        return root;
    }
private:
    int right_sum = 0;
};