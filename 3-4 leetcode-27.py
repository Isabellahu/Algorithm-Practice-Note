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
