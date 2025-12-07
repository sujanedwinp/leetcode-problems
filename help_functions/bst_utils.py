# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTTools(object):

    # ============================================================
    # 1️⃣ SORTED LIST → BALANCED BST
    # ============================================================
    def sorted_list_to_bst(self, nums):
        if not nums:
            return None

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(nums) - 1)

    # ============================================================
    # 2️⃣ UNSORTED LIST → NORMAL BST (INSERT MODE)
    # ============================================================
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def unsorted_list_to_bst(self, arr):
        root = None
        for x in arr:
            root = self.insert(root, x)
        return root

    # ============================================================
    # 3️⃣ LEVEL ORDER LIST → TREE (LeetCode format)
    # Example: [1,2,3,None,4]
    # ============================================================
    def level_list_to_tree(self, arr):
        if not arr:
            return None

        from collections import deque
        root = TreeNode(arr[0])
        q = deque([root])
        i = 1

        while q and i < len(arr):
            node = q.popleft()

            # left child
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i >= len(arr):
                break

            # right child
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root

    # ============================================================
    # BST → LIST in all 3 traversal forms
    # ============================================================
    def inorder(self, root):
        out = []
        def dfs(n):
            if not n: return
            dfs(n.left)
            out.append(n.val)
            dfs(n.right)
        dfs(root)
        return out

    def preorder(self, root):
        out = []
        def dfs(n):
            if not n: return
            out.append(n.val)
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return out

    def postorder(self, root):
        out = []
        def dfs(n):
            if not n: return
            dfs(n.left)
            dfs(n.right)
            out.append(n.val)
        dfs(root)
        return out

    def bst_to_lists(self, root):
        return {
            "inorder": self.inorder(root),
            "preorder": self.preorder(root),
            "postorder": self.postorder(root)
        }

    # ============================================================
    # TREE → LEVEL ORDER LIST (LeetCode style)
    # ============================================================
    def tree_to_level_list(self, root):
        if not root:
            return []

        from collections import deque
        q = deque([root])
        out = []

        while q:
            node = q.popleft()
            if node:
                out.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                out.append(None)

        # remove trailing None values
        while out and out[-1] is None:
            out.pop()

        return out
