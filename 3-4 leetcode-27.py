# 27. Remove Element

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k+=1

        nums = nums[:k]
        return len(nums)

    
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:

                nums[k+1] = nums[i+1]
                k+=1
        nums = nums[:k+1]
        return len(nums)
