# 144 Binary Tree Preorder Traversal
# 用栈的方式解决了前序遍历
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

# 前序遍历[根前]: 首先访问根结点，然后遍历左子树，最后遍历右子树

# 向量（Vector）是一个封装了动态大小数组的顺序容器  添加push_back()　　删除pop_back()
# stack 栈　　empty() 堆栈为空则返回真　push() 在栈顶增加元素　pop() 移除栈顶元素　size() 返回栈中元素数目　top() 返回栈顶元素
#  public 公共成员在类的外部是可访问，private或protected私有的成员和受保护的成员不能使用直接成员访问运算符 (.) 来直接访问
struct Command{
    string s;
    TreeNode* node;
    # 构造函数的初始化
    Command(string s, TreeNode* node): s(s), node(node) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if ( root == NULL )
            return res;
        # stack 存储命令
        # stack -> command -> res
        stack<Command> stack;
        stack.push( Command("go", root) );
        while ( !stack.empty() ) {
            Command command = stack.top();
            stack.pop();
            if ( command.s == "print" )
                res.push_back( command.node ->val );
            else{
                assert( command.s == "go" );
                # 栈操作：右子树入栈，左子树入栈，根结点入栈
                # 如果右子树存在
                if ( command.node -> right )
                    stack.push( Command("go", command.node -> right) );
                if ( command.node -> left )
                    stack.push( Command("go", command.node -> left) );
                stack.push( Command("print", command.node));
                
            }
        }
        return res;
         
    }
};


# 145. Binary Tree Postorder Traversal
# 后序遍历 
struct Command{
    string s;
    TreeNode* node;
    Command(string s, TreeNode* node): s(s), node(node) {}
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if ( root == NULL )
            return res;
        stack<Command> stack;
        stack.push( Command("go", root) );
        while ( !stack.empty() ) {
            Command command = stack.top();
            stack.pop();
            if ( command.s == "print" )
                res.push_back( command.node ->val );
            else{
                assert( command.s == "go" );
                # 栈操作：根结点入栈，右子树入栈，左子树入栈，
                stack.push( Command("print", command.node));
                if ( command.node -> right )
                    stack.push( Command("go", command.node -> right) );
                if ( command.node -> left )
                    stack.push( Command("go", command.node -> left) ); 
            }
        }
        return res;
            
    }
};



# 94. Binary Tree Inorder Traversal
# 中序遍历 
struct Command{
    string s;
    TreeNode* node;
    Command(string s, TreeNode* node): s(s), node(node) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if ( root == NULL )
            return res;
        stack<Command> stack;
        stack.push( Command("go", root) );
        while ( !stack.empty() ) {
            Command command = stack.top();
            stack.pop();
            if ( command.s == "print" )
                res.push_back( command.node ->val );
            else{
                assert( command.s == "go" );
                # 栈操作：右子树入栈，根结点入栈，左子树入栈
                if ( command.node -> right )
                    stack.push( Command("go", command.node -> right) );
                stack.push( Command("print", command.node));
                if ( command.node -> left )
                    stack.push( Command("go", command.node -> left) ); 
            }
        }
        return res;
            
    }
};
