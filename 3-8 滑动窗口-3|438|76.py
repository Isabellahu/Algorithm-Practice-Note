# leetcode-3

s = "kweqaasaadgas"
s = ""
s = " "

l = 0
r = -1
# 初始化长度为0
res = 0
# ASCII 码的长度是256位，每一位的索引表示一个字符的计数值
asc = [0] * 256

# 如果 s = " ", len(s)==1, l == 0 < 1 才能进入循环
while l < len(s):
    if r < len(s)-1 and asc[ord(s[r+1])] == 0:
        r += 1
        asc[ord(s[r])] += 1
        print('r =', r)
    else:
        asc[ord(s[l])] -= 1
        l += 1
    # print(s[l:r+1])
    res = max(res, r-l+1)
print(res)
