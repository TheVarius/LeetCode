class Solution(object):
    def leftRightDifference(self, nums):
        leftSum = []
        rightSum = []
        k1 = 0
        k2 = 0
        revNums = nums[::-1]
        leftSum.append(0)
        rightSum.append(0)
        for i in range(len(nums) - 1):
                k1 += nums[i]
                k2 += revNums[i]
                leftSum.append(k1)
                rightSum.append(k2)
        revRightSum = rightSum[::-1]
        res = [abs(a - b) for a, b in zip(leftSum, revRightSum)]
        return res
        
