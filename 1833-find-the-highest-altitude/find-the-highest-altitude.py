class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        p1 = 0
        p2 = 0
        curr = 0
        highest = 0


        while(p2 < len(gain)):
            curr = curr + gain[p2]
            highest = max(curr, highest)
            p1 += 1
            p2 += 1

        return highest

            


        