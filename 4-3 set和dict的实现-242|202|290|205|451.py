# leetcode-243

s = "anagram"
t = "nagaram"
dict1 = {}
dict2 = {}

for i in s:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

for i in t:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += 1

print(dict2 == dict1)

# leetcode-202
# set 记录出现的所有数字，以防重复计算
data = set()

while True:
    print(n)
    # sum 清零
    sum_v = 0
    while n > 0:
        sum_v += (n%10)*(n%10)
        n = n //10
    n = sum_v 
    if n == 1:
        return True
    if n in data:
        return False
    data.add(n)
    
    
# leetcode-290
pattern = "aaaa"
str = "dog cat cat dog"

# method1
# 建立两个字典，正向映射和反向映射
words = str.split(' ')
res = True
arr = {}
brr = {}
if len(pattern) != len(words):
    res = False
else:
    for i in range(len(str.split(' '))):
        if pattern[i] in arr:
            if arr[pattern[i]] != words[i]:
                res = False
        elif words[i] in brr:
            if brr[words[i]] != pattern[i]:
                res = False
        arr[pattern[i]] = words[i]
        brr[words[i]] = pattern[i]
print(res)


# method2
# set() 函数创建一个无序不重复元素集
# zip打包为元组, 判断set之后的长度是否相等
words = str.split(' ')
return len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))



# leetcode-205

# leetcode-451
