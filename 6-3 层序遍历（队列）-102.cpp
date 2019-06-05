# 102. Binary Tree Level Order Traversal
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        # 队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作
        # 队列: 先进先出  push(x)将x压入末端  pop()弹出第一个元素，不返回值 front()返回第一个元素  back()返回最后被压入的元素(队尾元素)
        # 栈：top() 返回第一个元素(栈顶元素)      
        
        # pair 模板类型，它只有两个 public 数据成员 first 和 second,  eg: pair<int, char>
        # make_pair<T1，T2> 函数模板是一个辅助函数，可以生成并返回一个 pair<T1，T2> 对象
        
        vector<vector<int>> res;
        if( root == NULL)
            return res;
        
        # 根节点入队，根节点出队，左右孩子入队; 循环队列进行出队，每次出队将其左右孩子入队
        queue< pair<TreeNode*, int> > q;
        # 根节点入队
        q.push( make_pair( root, 0 ) );
        while( !q.empty() ){
            TreeNode* node = q.front().first;
            int level = q.front().second;
            # 根节点出队
            q.pop();
            if(level == res.size())
                # vector<int>() 创建一个空vector
                res.push_back( vector<int>() );
            
            assert(level < res.size() );
            res[level].push_back( node->val );
            # 左右孩子入队
            if( node->left )
                q.push( make_pair( node->left, level + 1 ) );
            if( node->right )
                q.push( make_pair( node->right, level + 1 ) );
        }
        return res;
        
    }
};
