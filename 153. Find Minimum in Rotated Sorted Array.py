class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        minimum=nums[0]
        for i in range(1, n):
            if nums[i]<minimum:
                minimum=nums[i]
        return minimum
