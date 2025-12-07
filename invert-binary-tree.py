
# https://leetcode.com/problems/invert-binary-tree/

from help_functions import bst_utils 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def invertTree(root):
            if not root:
                return root
            
            temp=root.left
            root.left=root.right
            root.right=temp
            invertTree(root.left)
            invertTree(root.right)
            return root
        
        return bst_utils.BSTTools().tree_to_level_list(invertTree(root))
bsttool=bst_utils.BSTTools()

listtree=[4,2,7,1,3,6,9]
root=bsttool.level_list_to_tree(listtree)
print(listtree)
print(Solution().invertTree(root))