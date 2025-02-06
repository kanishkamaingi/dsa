class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:            
            if i not in operators :
                stack.append(int(i))
            else:                
                s = stack.pop()
                f = stack.pop()
                if i == "+":
                    stack.append(f + s)
                elif i == "-":
                    stack.append(f - s)
                elif i == "*":
                    stack.append(f * s)
                elif i == "/":
                    stack.append(int(float(f) / s))
                    
        return stack[-1]
        