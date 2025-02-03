class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        k = 0

        while i < j:
            _ = (j-i)

            if (height[i] <= height[j]):
                area = height[i] * _
                i += 1
                if k < area:
                    k = area                

            elif height[j] <= height[i]:
                area = height[j] * _
                j -= 1
                if k < area:
                    k = area              

        return k