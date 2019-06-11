# 279. Perfect Squares
# method 1
class Solution {
public:
    int numSquares(int n) {
        if(n <= 0)
            return 0;
        vector<int> res(n+1, INT_MAX);
        res[0] = 0;
        for(int i=1; i<=n; i++)
            for(int j=1; i-j*j>=0; j++)
                res[i] = min(res[i], res[i-j*j]+1); 
        return res[n];
        
    }
};

# method 2
class Solution {
public:
    int numSquares(int n) {
        queue<pair<int, int>> q;
        q.push( make_pair(n, 0) );//从n出发，到达n需要0步
        
        vector<bool> visited(n+1, false);
        visited[n] = true;
        while(!q.empty()){
            int num = q.front().first; //节点
            int step = q.front().second; //步数

            q.pop();

            if (num == 0)
                return step;
            
            for(int i = 1; ; i++){
                int a = num - i *i;
                if( a < 0 )
                    break;
                # 没有计算过的节点，以防重复
                if( visited[a]== false ){
                    q.push( make_pair(a, step + 1) );
                    visited[a] = true;
                    
                }
                
            }
                
        }
        # 抛出invalid_argument类异常对象
        throw invalid_argument("no answer!");
    }

            
};


    

    
