class Solution(object):
    def moveZeroes(self, nums):
       counter = 0
       for i in range(len(nums)):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter += 1
       ile_zer = len(nums) - counter
       nums[counter:] = [0] * ile_zer
