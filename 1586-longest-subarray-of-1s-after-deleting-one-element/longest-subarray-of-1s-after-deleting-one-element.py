class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        maxSubarrayOne = 0
        n = 0
        subArrayOne = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                n += 1
            else :
                subArrayOne += 1

            while n > 1:
                if nums[l] == 0:
                    n -= 1
                else:
                    subArrayOne -= 1
                l += 1
            maxSubarrayOne = max(maxSubarrayOne, subArrayOne)

        if maxSubarrayOne == len(nums):
            maxSubarrayOne -= 1
        
        return maxSubarrayOne
                    



        