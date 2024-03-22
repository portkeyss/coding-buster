/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(root == NULL)  return "[]";
        queue<TreeNode*> q;
        vector<string> qs;
        q.push(root);
        
        while(!q.empty()){
            TreeNode* t = q.front();
            q.pop();
            if(t) {
                qs.push_back(to_string(t->val));           
                q.push(t->left);
                q.push(t->right);
            }
            else {
                qs.push_back("null");
            }
        }
        int len = qs.size();
        while(qs[len-1] == "null") {
            len--;
        }
        
        string str = "[";
        for(int i = 0; i < len; i++){
            str += qs[i];
            str += ',';
        }
        str.pop_back();
        str += ']';
        return str; 
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data == "[]") return NULL;
        data = data.substr(1, data.size() - 2);
        stringstream data_ss(data);
        string seg;
        queue<TreeNode*> q;
        vector<string> ss;
        while(getline(data_ss, seg, ',')) {
            ss.push_back(seg);
        }
        int i = 0;
        TreeNode* root = new TreeNode(stoi(ss[i++]));
        q.push(root);
        while(!q.empty()){
            TreeNode* t_parent = q.front();
            q.pop();
            if(i >= ss.size()) break;
            string s1 = ss[i++];
            if(s1 != "null") {
                TreeNode *t_left = new TreeNode(stoi(s1));
                t_parent->left = t_left;
                q.push(t_left);
            }
            if(i >= ss.size()) break;
            string s2 = ss[i++];
            if(s2 != "null") {
                TreeNode *t_right = new TreeNode(stoi(s2));
                t_parent->right = t_right;
                q.push(t_right);
            }  
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));