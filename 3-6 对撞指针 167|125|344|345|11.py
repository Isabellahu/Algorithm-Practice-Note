# leetcode-167

numbers = [2,3,4,6,7,11,15]
target = 17

l = 0
r = len(numbers) - 1
print(r)

while l<r:
    if numbers[l] + numbers[r] == target:
        print([numbers[l], numbers[r]])
        print(l+1, r+1)
        break
    elif numbers[l] + numbers[r] < target:
        l+=1
    else:
        r-=1

        
        
# leetcode-125
# 只看数字和字母， 不考虑大小写
# 空字符串的处理
# method1
s = "A man, a plan, a canal: Panama"
ssd = "race a car"

# Python isalnum() 方法检测字符串是否由字母和数字组成
new_s = [i for i in s.upper() if i.isalnum()]
error = 0
l = 0
r = len(new_s)-1
       
while l<r:
    if new_s[l] != new_s[r]:
        error = 1        
    l+=1
    r-=1 

print(error==0)


##method2
# 直接比较原字符串与回文序列
s = "A man, a plan, a canal: Panama"
s = "race a car"

# Python isalnum() 方法检测字符串是否由字母和数字组成
new_s = [i for i in s.upper() if i.isalnum()]
# a[i:j:s]  s表示步进，缺省为1
# a[i:j:1] == a[i:j]
# a[::-1] 回文序列
print(new_s == new_s[::-1])


# leetcode-344
# method1
s = "A man, a plan, a canal: Panama"
out = "amanaP :lanac a ,nalp a ,nam A"
print(s[::-1]==out)
  
# method2
a =''.join([s[i] for i in range(len(s)-1, -1, -1)])
print(a==out)



# leetcode-345
s = "leetcode"
yuanyin = ['a', 'e', 'i', 'o', 'u']

l = 0
r = len(s) - 1
s = list(s)

while l < r:
    while l < r and s[l].lower() not in yuanyin:
        l += 1

    while l < r and s[r].lower() not in yuanyin:
        r -= 1
    if l != r:
        s[l], s[r] = s[r], s[l]

    l +=1
    r -=1
s = ''.join(i for i in s)
print(s)

# leetcode-11
height = [2,3,4,5,18,17,6]
l = 0
r = len(height) - 1
container = min(height[l], height[r]) * (r-l)

while l < r:
    if (min(height[l], height[r]) * (r-l)) > container:
        container = min(height[l], height[r]) * (r-l)
    # 比较左右大小， 较大值的指针不动
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(container)
