class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        my_str = ''
        
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                my_str = my_str + word1[i]
            if i < len(word2):
                my_str = my_str + word2[i]

        return my_str
        