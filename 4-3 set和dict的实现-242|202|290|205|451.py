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
