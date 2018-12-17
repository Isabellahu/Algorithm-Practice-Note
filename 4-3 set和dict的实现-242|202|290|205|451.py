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

# leetcode-205

# leetcode-451
