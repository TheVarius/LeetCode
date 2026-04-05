class Solution(object):
    def frequencySort(self, nums):
        counts = {}
        res = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        sorted_items = sorted(counts.items(), key=lambda x: (x[1], -x[0]))
                
        
        for k, v in sorted_items:
            for j in range(v):
                res.append(k)
        return res



        
