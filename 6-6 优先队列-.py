# 347. Top K Frequent Elements

# 排序算法
# 时间复杂度：O()，其中 n 表示数组的长度。
# 空间复杂度：O(n)，最极端的情况下（每个元素都不同），用于存储元素及其频率的 Map 需要存储 n 个键值对

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 创建字典哈希表，无序 　　key,value 元素，频率
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        # 按照频率进行排序
        freq_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(freq_dict[i][0])
        return res

# 最小堆
# 时间复杂度：O(nlogk)，其中 n 表示数组的长度。首先，统计元素的频率，时间复杂度是 O(n) 的；接着，遍历用于存储元素频率的 map，如果元素的频率大于最小堆中顶部的元素，则将顶部的元素删除并将该元素加入堆中，时间复杂度是 O(nlogk) 的；最后，弹出堆中的元素所需的时间复杂度是 O(klogk) 的。因此，总的时间复杂度是 O(nlogk) 
# 空间复杂度：O(n),最坏情况下（每个元素都不同），map 需要存储 n 个键值对，优先队列需要存储 k 个元素

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 创建字典哈希表，无序 　　key,value 元素，频率
        dict1 = {}
        for i in nums:
            # 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值
            dict1[i] = dict1.get(i, 0) + 1
        # 创建优先队列 　维护一个大小为k的最小堆，使得堆中的元素即为前k个高频元素
        # heapq.heappush(heap,item)  # heap为定义堆，item 增加的元素
        # heapq.heappop(heap)        # 删除最小的值
        # heapq.heapreplace(heap, item)     #删除最小元素值，添加新的元素值
        pq = []
        for key, value in dict1.items():
            if len(pq) < k:
                heapq.heappush(pq, (value, key))
            elif value > pq[0][0]:
                heapq.heapreplace(pq, (value, key))
        res = []      
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res

# 桶排序
# 时间复杂度：O(n)，其中 n表示数组的长度。
# 空间复杂度：O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 创建字典哈希表，无序 　　key,value 元素，频率
        #生成字典映射
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i,0) + 1
        max_value = max(dict1.values())
        # 用数组表示每个桶，从0到最大出现次数，一共是（max_value+1）个桶
        tong = [[] for i in range(max_value+1)]
        for key, value in dict1.items():
            # 将元素key放入桶中
            tong[value].append(key)
        res = []
        # 按桶索引排序
        for i in range(max_value,-1,-1):
            # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值
            if tong[i]:
                res.extend(tong[i])
            if len(res) == k:
                break
        return res   
