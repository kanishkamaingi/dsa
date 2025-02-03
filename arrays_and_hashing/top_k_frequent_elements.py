class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = dict()

        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        sorted_arr = sorted(my_dict, key = lambda x: my_dict[x], reverse = True)

        return list(sorted_arr[:k])
