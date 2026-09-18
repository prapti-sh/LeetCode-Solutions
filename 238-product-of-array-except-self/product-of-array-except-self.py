class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prd = 1
        l = len(nums)
        prefix = 1
        suffix = 1
        ans = [1] * l


        for i in range(0, l):
            ans[i] = prefix
            prefix *= nums[i]

        print(prefix)
        
        for i in range(l-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

      
        return ans 


            
