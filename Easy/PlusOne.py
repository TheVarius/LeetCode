class Solution(object):
    def plusOne(self, digits):
        res = 0
        dupa = []
        for i in range(len(digits)):
            res += digits[i] * 10 ** (len(digits) - i - 1)
        res += 1
        digits[:] = [int(x) for x in str(res)]
        return digits
