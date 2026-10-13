class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = -1
        right = sum(nums) 
        left = 0

        if left == right - nums[0]:
            return 0
        right = right - nums[0]

        for i in range(1, len(nums)):

            left = left + nums[i-1]
            if i < len(nums):
                right = right - nums[i]
            else:
                right = 0

            if left == right:
                return i
        return -1



            




        