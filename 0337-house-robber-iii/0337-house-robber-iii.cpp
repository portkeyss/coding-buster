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
    int rob(TreeNode* root) {       
        vector<int> res = robber(root);
        return std::max(res[0], res[1]);
    }
private:
    vector<int> robber(TreeNode* root){
        vector<int> max(2);//max[0] means max money robbed in current subtree if its root node not robbed, max[1] means robbed. This way of redefining the rob function effectively eliminates the possible overlaps of subtrees, saving storage space typically used in DP problems.
        if(root == nullptr) return max;        
        vector<int> left = robber(root->left);
        vector<int> right = robber(root->right);
        max[0] = std::max(left[0], left[1]) + std::max(right[0],right[1]);
        max[1] = root->val + left[0] + right[0];
        return max;
    }
};