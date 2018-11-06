# 二分查找法
def find_med(a, target):
    #[l, r]
    l = 0
    r = len(a)-1
    
    while(l<=r):
#        # 整形溢出
#        med = (l+r)//2
        med = l + (r-l)//2
        if target == a[med]:
            return med
        elif target > a[med]:
            l = med + 1
        elif target < a[med]:
            r = med - 1
        
arr = []
for i in range(100):
    arr.append(i)
c = find_med(arr, 22)
print(arr[c])
