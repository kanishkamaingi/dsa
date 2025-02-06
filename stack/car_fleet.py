class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
        my_list = [(p, s) for p, s in zip(position, speed)]

        my_list.sort(reverse = True)

        for (p, s) in my_list:
            t = float(target-p)/s
            if not stack or stack[-1] < t :
                stack.append(t)

        return len(stack)
        