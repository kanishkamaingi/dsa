class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
            

        return nums[l]
        