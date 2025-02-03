class Solution(object):
    def twoSum(self, nums, target):
        dict1 = dict()
        
        for i in range(len(nums)):            
            if target - nums[i] in dict1:
                return i, dict1[target-nums[i]]
            else:
                dict1[nums[i]] = i
        