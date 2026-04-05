class Solution(object):
    def shuffle(self, nums, n):
        res = []
        l1 = nums[:n]
        l2 = nums[n:]
        for x,y in zip(l1,l2):
            res.append(x)
            res.append(y)
        return res
        
