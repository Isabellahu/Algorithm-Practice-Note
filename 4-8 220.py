# leetcode - 220. Contains Duplicate III
nums = [0, 2147483647]
k = 1
t = 2147483647

# Python3 整型是没有限制大小的，可以当作 Long 类型使用
d = set()
# 分情况用不同的策略
if len(nums) < 3:
    for i in range(len(nums)):
        for _ in d:
            if (nums[i] - t) <= _ <= (nums[i] + t):
                return True
        d.add(nums[i])
        # 添加元素之后，窗口的长度不能超过K
        if len(d) == k+1:
            d.remove(nums[i-k])
else:
    d = set()
    for i in range(len(nums)):
        # # 判断
        for m in range((nums[i]) - t, (nums[i]) + t+1):
            if m in d:
                return True
        d.add(nums[i])
        # 添加元素之后，窗口的长度不能超过K
        if len(d) == k+1:
            d.remove(nums[i-k])
return False
