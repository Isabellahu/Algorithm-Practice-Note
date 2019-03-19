# method one
# time: o(n)
# space:o(n)
# 在c++中，vector是一个十分有用的容器
# (1)头文件#include<vector>　　(2)创建vector对象，vector<int> vec;　　(3)尾部插入数字：vec.push_back(a);
void moveZeroes(vector<int>& nums) {
    vector<int> nozero;
    for( int i = 0; i < nums.size(); i++ )
        if( nums[i] )
            nozero.push_back(nums[i]);
    for( int i = 0; i < nozero.size(); i++)
        nums[i] = nozero[i];
    for( int i = nozero.size(); i < nums.size(); i++)
        nums[i] = 0;
        
        
        
# method two      
# time: o(n)
# space:o(1)
# 在c++中，vector是一个十分有用的容器
# (1)头文件#include<vector>　　(2)创建vector对象，vector<int> vec;　　(3)尾部插入数字：vec.push_back(a);
void moveZeroes(vector<int>& nums) {
    # [0,,,k)  非0元素
    int k = 0; 
    for( int i = 0; i < nums.size(); i ++)
        if( nums[i] )
            # 防止自身交换
            if( i != k) 
                swap( nums[k++], nums[i] );
            else
                k ++;
