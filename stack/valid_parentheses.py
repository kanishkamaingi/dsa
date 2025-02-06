class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        _ = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in s:
            if i not in _:
                stack.append(i)
            else:
                if stack:
                    if stack[-1] == _[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
            
        
        if stack:
            return False
        else:
            return True
            
        
        