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
