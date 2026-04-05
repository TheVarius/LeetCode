class Solution(object):
    def reversePrefix(self, s, k):
        l = s[:k]
        a = l[::-1]
        word = a + s[k:]

        return word
        
