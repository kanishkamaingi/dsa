class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]

        stored_prod = 1
        for i in range(len(nums)-2, -1, -1):
            stored_prod *= nums[i+1]
            answer[i] *= stored_prod

        return answer        