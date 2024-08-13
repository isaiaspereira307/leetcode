# 129 Sum Root to leaf Numbers
# Depth first search

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = ""
        def dfs(root, total):
            if root:
                if root.left is None and root.right is None:
                    return int(total + str(root.val))
                total += str(root.val)
                return dfs(root.left, total) + dfs(root.right, total)
            return 0
        return dfs(root, total)

