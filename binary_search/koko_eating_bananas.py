class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low, high = 1, max(piles)
        res = high
        
        while low <= high:
            total = 0
            mid = (low + high) // 2

            for num in piles:
                total += math.ceil(float(num) / mid)

            if total <= h:
                res = mid
                high = mid - 1

            else:
                low = mid + 1
        
        return res
                

        