class Solution(object):
    def recoverOrder(self, order, friends):
        indices = []
        for i in order:
            if i in friends:
                indices.append((i))

        return indices
