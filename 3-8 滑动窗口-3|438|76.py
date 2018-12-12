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



# leetcode-438
s = "baa"
p = "aa"


if p == '' or s == '' or len(s) < len(p):
    res = []

else:
    num = len(p)
    # 初始化
    res = []
    # ASCII 码有255个
    asc = [0] * 256
    for i in range(len(p)):
        asc[ord(p[i])] += 1

    l = 0
    r = -1

    while l < len(s):
        # 可能p中有重复元素
        if r < len(s) - 1 and asc[ord(s[r+1])] > 0:
            print('###')
            print('l =', l)
            print('r = ', r)
            print('num = ', num)
            asc[ord(s[r+1])] -= 1
            r += 1
            num -= 1
        else:
            # print('###')
            # print('l =', l)
            # print('r = ', r)
            # print('num = ', num)
            if s[l] in p:
                asc[ord(s[l])] += 1
                num += 1
            if s[l] not in p:
                r = l
            l +=1
        if num == 0:
            asc[ord(s[l])] += 1
            num += 1
            # res.append(s[l:r+1])
            res.append(l)
            l += 1

print(res)


