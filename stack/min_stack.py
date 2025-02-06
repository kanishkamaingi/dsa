class MinStack(object):

    def __init__(self):
        self._ = []
        self.__ = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._.append(val)

        if self.__ and self.__[-1] < val:
            val = self.__[-1]
        
        self.__.append(val)

            
        

    def pop(self):
        """
        :rtype: None
        """
        self._.pop()
        self.__.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self._[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.__[-1]
        