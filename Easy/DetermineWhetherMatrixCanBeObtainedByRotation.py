class Solution(object):
    def findRotation(self, mat, target):
        def get_copy(m):
            return [row[:] for row in m]

        def deg90(m):
            res = get_copy(m)
            n = len(res)
            for i in range(n):
                for j in range(i + 1, n):
                    res[i][j], res[j][i] = res[j][i], res[i][j]
            for row in res:
                row[:] = row[::-1]
            return res

        def deg180(m):
            res = get_copy(m)
            res[:] = res[::-1]
            for row in res:
                row[:] = row[::-1]
            return res

        def deg270(m):
            res = get_copy(m)
            n = len(res)
            for i in range(n):
                for j in range(i + 1, n):
                    res[i][j], res[j][i] = res[j][i], res[i][j]
            res[:] = res[::-1]
            return res

        if mat == target: return True
        if deg90(mat) == target: return True
        if deg180(mat) == target: return True
        if deg270(mat) == target: return True
        
        return False
