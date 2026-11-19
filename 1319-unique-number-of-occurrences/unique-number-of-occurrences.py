

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        arrDict = dict.fromkeys(arr, 0)

        for a in arr:
            arrDict[a] += 1

        arrSet = set(arrDict.values())

        if len(arrSet) == len(arrDict.values()):
            return True
        else: 
            return False
        
        