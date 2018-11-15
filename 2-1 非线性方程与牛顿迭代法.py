# 二分逼近法算法实现

num = 0.000000000000001
def func(x):
    return (2.0*x*x + 3.2*x - 1.8)

a = 0
b = 2
mid = (a+b)/2.0
while((b-a)> num):
    if (func(a) * func(mid) > 0.0):
        a = mid
    else:
        b = mid
        
    mid = (a+b)/2.0
print(mid)
print(func(mid))


# 牛顿迭代法

nums = 0.000000001
def cal(x):
    return ((x+nums)+(x-nums))/(nums*2)
def func(x):
    return (2.0*x*x + 3.2*x - 1.8)
    print(2.0*x*x + 3.2*x - 1.8)
    
i = 0
x0 = 0.44446
while (i<10):
    print(i)
    x0 = x0 - func(x0)/cal(x0)
    i+=1
   
    
print(x0) 
print(func(x0))
