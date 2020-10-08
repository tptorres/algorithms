def rightSideView(self, root: TreeNode) -> List[int]:
    res = []
    self.helper(root, res, 1)
    return res


def helper(self, root, res, level):
    if root is None:
        return
    if len(res) < level:
        res.append(root.val)
    self.helper(root.right, res, level+1)
    self.helper(root.left, res, level+1)
