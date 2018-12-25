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



# leetcode-15. 3Sum
nums = [-2,0,0,2,2]

res = []
nums.sort()
print('nums =', nums)
for i in range(len(nums)-2):
    # 去重
    if i > 0 and nums[i] == nums[i-1]:
        # continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环
        continue
    l = i + 1
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == -nums[i]:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1
            # 添加列表之后去重，以防相同元素重复被使用（有序列表，相同元素挨在一起）
            while l < r and nums[l] == nums[l-1]:
                l += 1
            while l < r and nums[r] == nums[r+1]:
                r -= 1
        elif nums[l] + nums[r] < -nums[i]:
            l += 1
        else:
            r -= 1
print(res)


# leetcode-18
# leetcode-16
