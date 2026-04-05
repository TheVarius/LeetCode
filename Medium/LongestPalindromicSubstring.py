class Solution(object):
    def longestPalindrome(self, s):
        substrings = []
        res = ""
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                word = (s[start : start + length])
                if word == word[::-1]:
                    return word
                
 
