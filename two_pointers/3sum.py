class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = list()

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            target = -(nums[i])
            j = i+1
            k = len(nums)-1

            while j < k:
                _ = nums[j] + nums[k]
                if _ == target:
                   res.append([nums[i], nums[j], nums[k]])
                   j += 1
                   k -= 1

                   while j < k and nums[j] == nums[j-1]:
                    j += 1
                   
                   while j < k and nums[k] == nums[k+1]:
                    k -= 1
                   
                   
                elif _ < target:
                    j +=1
                else:
                    k -=1
                    
        return res 
        