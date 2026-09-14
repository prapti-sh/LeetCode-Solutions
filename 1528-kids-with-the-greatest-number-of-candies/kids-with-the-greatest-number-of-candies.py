class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = 0
        res = []
        for candy in candies:
            if candy > maxCandy:
                maxCandy = candy
        
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res


        