class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = 0
        h = len(matrix) - 1

        while l <= h:
            m = (l + h) // 2
            if target < matrix[m][0]:
                h = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        
        if l > h:
            return False
        
        r = (l + h) // 2

        low = 0
        high = len(matrix[0]) - 1
                 
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[r][mid]:
                high = mid - 1
            elif target > matrix[r][mid]:
                low = mid + 1
            else:
                return True
            

        
        return False

        