class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        counts=[0]*(n+1)
        for i in range(1, n+1):
            counts[i]=counts[i//2]+(i&1)
        return counts
        
