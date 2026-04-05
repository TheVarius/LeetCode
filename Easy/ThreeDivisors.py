class Solution(object):
    def isThree(self, n):
        counter = 2
        for i in range(2, n//2 + 1):
            if n % i == 0:
                counter += 1
        if counter == 3:
            return True
        return False 

        
