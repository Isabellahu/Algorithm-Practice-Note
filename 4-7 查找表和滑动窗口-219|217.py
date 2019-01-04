# leetcoed-219. Contains Duplicate II
nums = [1,2,3,1,2,3]
k = 2

d = set()     
for i in range(len(nums)):
    # 寻找窗口d中的是否和新元素相同
    if nums[i] in d:
        return True
    # 插入新的元素
    d.add(nums[i])
    # 保证d中长度为k+1
    if len(d) == k+1:
        d.remove(nums[i-k])
return False


# leetcoed-217. Contains Duplicate
d = set()
for i in range(len(nums)):
    if nums[i] in d:
        return True
    d.add(nums[i])
return False
