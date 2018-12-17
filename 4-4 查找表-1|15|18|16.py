# leetcode-1. Two Sum
nums = [2, 7, 11, 15]
target = 9
# method 1
# 存储nums中的每个元素
res = {}
for i in range(len(nums)):
    tar_value = target-nums[i]
    if tar_value in res:
        print(res[tar_value], i)
    else:
        res[nums[i]] = i
print('dict = ', res)

# method 2
# 存储target-nums的每个元素
res = {}
for i in range(len(nums)):
    if nums[i] in res:
        print(res[nums[i]], i)
    else:
        res[target - nums[i]] = i
print('dict = ', res)



# leetcode-15

# leetcode-18
# leetcode-16
