class Solution(object):
    def convertTemperature(self, celsius):
        ans = []
        ans.append(celsius + 273.15)
        ans.append(celsius * 1.80 + 32.00)
        return ans 
       
