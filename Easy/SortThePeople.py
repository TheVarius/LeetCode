class Solution(object):
    def sortPeople(self, names, heights):
        dict = {}
        res = []
        for i in range(len(names)):
            dict[heights[i]] = names[i]
        temp = sorted(dict.items(), key=lambda item: item[0], reverse = True)
        
        for i in temp:
            res.append(i[1])
        return res
        
