class Solution(object):
    def findGCD(self, nums):
       b = min(nums)
       a = max(nums)
       temp  = 0
       while a % b != 0:
            temp = a
            a = b
            b = temp % b
       return b
