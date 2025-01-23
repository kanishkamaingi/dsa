class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for _ in set(s):
            if s.count(_) != t.count(_):
                return False
        
        return True