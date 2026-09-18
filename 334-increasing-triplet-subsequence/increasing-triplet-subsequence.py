class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mn = float('inf')
        mx = float('inf')
        
        for n in nums:
            if n <= mn:
                mn = n
            elif n <= mx:
                mx = n
            else:
                return True
            
        
        return False

        