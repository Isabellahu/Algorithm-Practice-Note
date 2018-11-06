# leetcode-283 
# MOVE ZEROS

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def move_zeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for i in range(j,len(nums)):
        nums[i] = 0
    print(nums)
    
move_zeros([1,2,0,4,0,9,0,2,4])
