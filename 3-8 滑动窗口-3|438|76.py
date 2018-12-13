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


# leetcode-76
'''
通过两个数组分别记录目标字符串每个字母出现次数 和 记录窗口内每个字母出现次数
如果窗口数组中的字母对应次数 <= 目标数组中的字母对应次数， 则完成一次对应
当符合要求的字母全部对应，让左边界不断累加直到指向符合要求的数组，最短长度不断更迭
'''
s = "ABC"

t = "ABC"

min_length = len(s)
num = 0

if s == '' or t == '' or len(s) < len(t):
    res = ""

else:
    res = ""
    # 记录目标字符串每个字母出现次数
    t_char = [0] * 128
    for i in range(len(t)):
        t_char[ord(t[i])] += 1

    # 用于记录窗口内每个字母出现次数
    window_char = [0] * 128

    l = 0

    for r in range(len(s)):
        window_char[ord(s[r])] += 1
        # 如果窗口数组中的字母对应次数 <= 目标数组中的字母对应次数， 则完成一次对应
        if t_char[ord(s[r])] >= window_char[ord(s[r])]:
            num += 1
        # 当符合要求的字母全部对应，，
        if num == len(t):
            # 让左边界不断累加直到指向符合要求的数组
            while l < r and t_char[ord(s[l])] < window_char[ord(s[l])]:
                window_char[ord(s[l])] -= 1
                l += 1
            # 最短长度不断更迭
            if r - l < min_length:
                min_length = r - l
                res = s[l:r+1]
                print(res)
            # 把开头的这个匹配字符跳过，并将匹配字符数减1
            window_char[ord(s[l])] -= 1
            num -= 1
            l += 1

print('res = ', res)
