class Solution(object):
    def reversePrefix(self, word, ch):
        c = 0
        ans = ""
        for i in range(len(word)):
            if word[i] == ch and c == 0:
                temp = word[:i+1]
                temp1 = temp[::-1]
                ans = temp1 + word[i+1:]
                c += 1
        if ch not in word:
            return word
        return ans



        
