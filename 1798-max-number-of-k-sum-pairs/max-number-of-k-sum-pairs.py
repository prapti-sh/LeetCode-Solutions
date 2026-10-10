class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        count = 0
        nums.sort()

        while l < r:
            total = nums[l] + nums[r]

            if total == k:
                count += 1
                l += 1
                r -= 1 
            elif total < k:
                l += 1
            else:
                r -= 1

        return count

        