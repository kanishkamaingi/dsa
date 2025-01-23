class Solution(object):
    def groupAnagrams(self, strs):
        my_dict = dict()

        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word in my_dict:
                my_dict[sorted_word].append(i)
            else:
                my_dict[sorted_word] = [i]

        return list(my_dict.values())