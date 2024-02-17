class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        globalmax=currentmax=nums[0]
        for i in range(1, n):
            currentmax=max(nums[i], currentmax+nums[i])
            if currentmax > globalmax:
                globalmax=currentmax
        return globalmax
