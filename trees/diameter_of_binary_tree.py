# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def recDepth(subtree):
            if subtree == None:
                return 0
            else:
                return 1+(max(recDepth(subtree.left), recDepth(subtree.right)))

        return recDepth(root.left) + recDepth(root.right)
        