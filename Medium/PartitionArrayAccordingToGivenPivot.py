class Solution(object):
    def pivotArray(self, nums, pivot):
        t1 = []
        t2 = []
        t3 = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                t1.append(nums[i])
            elif nums[i] == pivot:
                t2.append(nums[i])
            elif nums[i] > pivot:
                t3.append(nums[i])
        return t1 + t2 + t3
