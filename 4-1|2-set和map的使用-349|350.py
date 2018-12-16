# set 键
# set函数是一个无序不重复元素集 
# 基本功能包括关系测试和消除重复元素
a = [1,2,1,3,4,3,2,2,2]
print(list(set(a)))

x = set('abcd')
y = set(['a','v','b'])
print(list(x&y))
print(list(x|y))
print(list(x-y))
'''
[1, 2, 3, 4]
['b', 'a']
['b', 'a', 'd', 'v', 'c']
['c', 'd']
'''
# map 键值对应
# 接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素
#，并把结果作为新的list返回。
print(list(map(lambda x: x + 10, range(10))))
# 计算复杂的函数，比如，把这个list所有数字转为字符串
print(list(map(str, [1,3,4,5])))

# leetcode-349. Intersection of Two Arrays
nums1 = [1,2,2,1]
nums2 = [2,2]
print(list(set(nums1)&set(nums2)))


# leetcode-350. Intersection of Two Arrays II
nums1 = [1,2,1,3,1,4,4,4,4]
nums2 = [2,2,4,4,4]


res = []
# list转化为字典
def list_to_dict(num1):
    a = {}
    for i in num1:
       a[i] = num1.count(i)
    print(a)
    return a

dict1 = list_to_dict(nums1)
dict2 = list_to_dict(nums2)
# 字典1中的元素如果存在字典2中，则取最小的对应值extend到数组res
for i in dict1:
    if dict2.get(i):
#        print(i,' ',dict2[i])
        res.extend([i]*(min(dict2[i],dict1[i])))
print(res)
