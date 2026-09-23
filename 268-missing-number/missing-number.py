class Solution(object):
    def missingNumber(self, nums):
        actualSum = sum(n for n in nums)
        l = len(nums)
        origSum = (l * (l+1))/2

        return int(origSum - actualSum)
        