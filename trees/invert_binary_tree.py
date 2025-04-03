# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rec(self, subtree):
        if subtree == None:
            return subtree
        else:
            
            subtree.left, subtree.right  = self.rec(subtree.right),self.rec(subtree.left)
            return subtree
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        

        return self.rec(root)
        