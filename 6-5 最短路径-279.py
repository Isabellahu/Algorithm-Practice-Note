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
