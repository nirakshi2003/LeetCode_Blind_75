class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        actualsum=sum(nums)
        expectedsum=n*(n+1)//2 
        missing_num=expectedsum-actualsum
        return missing_num
