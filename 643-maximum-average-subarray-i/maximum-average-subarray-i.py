class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        sumToK = sum(nums[:k])
        maxAvg = sumToK/float(k)
        r = k


        while r < len(nums):
            sumToK += nums[r] - nums[r-k]
            maxAvg = max(sumToK/float(k), maxAvg)
            r += 1
        return maxAvg
        