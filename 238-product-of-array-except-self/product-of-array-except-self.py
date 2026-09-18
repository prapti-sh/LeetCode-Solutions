class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prd = 1
        l = len(nums)
        prefix = [1] * (l+1)
        suffix = [1] * (l+1)
        ans = [1] * l


        for i in range(0, l):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(l-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        for i in range(l):
            pre = 1
            suff = 1
            if i-1 >= 0:
                pre = prefix[i-1]
            if i+1 <= l:
                suff = suffix[i+1]
            ans[i] = pre * suff
        return ans 


            
