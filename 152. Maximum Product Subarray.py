class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        currentmax=currentmin=globalmax=nums[0]
        for i in range(1, n):
            if nums[i]<0:
                currentmax, currentmin=currentmin, currentmax
            currentmax=max(nums[i], nums[i]*currentmax)
            currentmin=min(nums[i], nums[i]*currentmin)
            globalmax=max(globalmax, currentmax)
        return globalmax
