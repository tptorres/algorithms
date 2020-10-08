def sumNumbers(self, root: TreeNode) -> int:
    return self.sum_helper(root, 0)


def sum_helper(self, root, current):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 10 * current + root.val

    new_current = 10 * current + root.val
    return self.sum_helper(root.left, new_current) + self.sum_helper(root.right, new_current)
