class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        l = 0
        h = len(nums)-1

        while index == -1 and l <= h:
            mid = (l + h) // 2
            if target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                index = mid

        return index
        