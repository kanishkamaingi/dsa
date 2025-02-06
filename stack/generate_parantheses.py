class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def recParentheses(o, c):
            if o == n and c == n:
                res.append("".join(stack))

            else:
                if o < n:
                    stack.append("(")
                    recParentheses(o + 1, c)
                    stack.pop()
                
                if c < o:
                    stack.append(")")
                    recParentheses(o, c + 1)
                    stack.pop()

        
        recParentheses(0, 0)
        return res