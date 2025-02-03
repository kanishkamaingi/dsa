class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(numbers) == 2:
            return 1,2

        i = 0
        j = len(numbers)-1

        while i < j:
            _ = numbers[i] + numbers[j]
            if _ == target:
                return i+1, j+1

            elif _ < target:
                i += 1

            else:
                j -= 1
