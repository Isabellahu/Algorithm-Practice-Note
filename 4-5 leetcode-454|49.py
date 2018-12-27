# leetcode-454. 4Sum II

# hash查找效率高，dict的值存储sum出现次数
A = [0,0,0,0]
B = [0,0,0,0]
C = [-1,1]
D = [1,-1]

dict1 = {}
num = 0
for i in A:
    for j in B:
        if i+j not in dict1:
            dict1[i+j] = 0
        dict1[i+j] += 1
print(dict1)

res = 0
for i in C:
    for j in D:
        if -(i+j) in dict1:
            res += dict1[-(i+j)]
print(res)


# 49. Group Anagrams
# sorted（）将字符串排序
# 保存dict的值为list，使得下一次append（）
d = {}                                         
res_set = set()                                
                                               
for i in strs:                                 
    key = ''.join(sorted(i))                   
    if key in d:                               
        d[key].append(i)                       
    else:                                      
        # value 第一次保存为list                     
        d[key] = [i]                           
                                               
print(list(d.values()))                        
                                               
