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

