class Solution(object):
    def diagonalSum(self, mat):
        res = 0
        for i in range(len(mat)):
            res += mat[i][i] 
        for j in range(len(mat) - 1, -1, -1):
            res += mat[j][len(mat) - j - 1]
        if len(mat) % 2 != 0:
            res -= mat[len(mat) // 2][len(mat) // 2]
        return res

        
