# Leetcode-209
s = 5
nums = [2,2]

l = 0
r = -1
sum = 0
res = len(nums) + 1
while l < len(nums)-1:
    if r < len(nums)-1 and sum < s:
        r += 1
        sum += nums[r]
    else:
        # res = min(res, l-r+1)
        sum -= nums[l]
        l += 1
    if l-r+1 < res and sum >= s:
        print('len =', r-l+1)
        res = min(r-l+1, res)
    print(nums[l:r+1])
    print('###########   sum = ', sum)
# 可能整个list元素相加都小于s， 则返回0
if res == len(nums) + 1:
    res = 0
print('res =', res)
