class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        maxLen = 0
        n = 0

        for r in range(len(nums)):


            if nums[r] == 0:
                n  += 1
            while n > k and l<len(nums):
                if(nums[l] == 0):
                    n -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
        
        return maxLen



            
        