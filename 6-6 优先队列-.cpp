# 堆的底层实现
# 347. Top K Frequent Elements
class Solution {
public:
    # 优先队列　priority_queue<Type, Container, Functional> 
    # 其中, Type 为数据类型  Container 为保存数据的容器  Functional 为元素比较的方式
    # priority_queue<int> pq1; // 默认是最大堆
    # priority_queue<int, vector<int>, greater<int>> pq2; // 最小堆
    # priority_queue<int, vector<int>, function<bool(int,int)>> pq  使用自定义Comparator 
    
    # unordered_map 内部实现了一个哈希表，记录元素的hash值
    # unordered_map内部元素是无序的，而map中的元素是按照二叉搜索树存储（用红黑树实现），进行中序遍历会得到有序遍历
    # (*it).first;   the key value  (*it).second   the mapped value
    # unordered_map<key,T>::iterator it; 
    # for(unordered_map<key,T>::iterator iter=mp.begin();iter!=mp.end();iter++)
    #      cout<<"key value is"<<iter->first<<" the mapped value is "<< iter->second;

    # 给定一个非空数组，返回前Ｋ个出现频率最高的元素
    # 解法：　字典存放元素和频率，创建优先队列保存前Ｋ个（频率，元素）自动最小堆排序
    # 时间复杂度：０(nlogk)
    vector<int> topKFrequent(vector<int>& nums, int k) {
        # 创建字典哈希表，无序 　　key,value 元素，频率
        unordered_map<int,int> freq;
        for( int i = 0; i < nums.size(); i++ )
            freq[nums[i]] ++;
        cout << freq.size();
        # 创建优先队列 　最小堆　　频率，元素
        priority_queue< pair<int,int>, vector<pair<int, int>>, greater<pair<int,int>> > q;
        
        for( unordered_map<int,int>::iterator iter=freq.begin(); iter!=freq.end(); iter++ ){
            # cout << "key is" << iter->first << "value is" << iter->second;
            if( q.size() == k ){
                # 当前字典元素的频率 > 最小队列元素的频率
                if( iter->second > q.top().first ){
                    q.pop();
                    q.push( make_pair( iter->second, iter->first ) );
                }
            }
            else
                q.push( make_pair( iter->second, iter->first ) );
        }
        
        vector<int> res;
        while( !q.empty() ){
            # 添加最小队列的元素
            res.push_back( q.top().second );
            q.pop();
        }
        return res;
    }
};
