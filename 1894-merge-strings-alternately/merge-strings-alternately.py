class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        p1 = 0
        p2 = 0

        while p1 < len(word1) and p2 < len(word2):
            res += word1[p1] + word2[p2]
            p1 +=1
            p2 +=1
        
        if p1 < len(word1):
            res += word1[p1::]
        if p2 < len(word2):
            res += word2[p2::]

        return res



        

