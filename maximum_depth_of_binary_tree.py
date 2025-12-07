
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from help_functions import bst_utils

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
    



bsttool=bst_utils.BSTTools()

listtree=[0,0,0,0,None,None,0,None,None,None,0]
root=bsttool.level_list_to_tree(listtree)
print(listtree)
print(Solution().maxDepth(root))
        