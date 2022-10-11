# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        l_node = [root]
        l_val = [root.val]
        while l_node:
            cur = l_node.pop(0)
            temp = l_val.pop(0)
            if not cur.left and not cur.right:
                if temp == sum:
                    return True
                continue
            if cur.left:
                l_node.append(cur.left)
                l_val.append(temp + cur.left.val)
            if cur.right:
                l_node.append(cur.right)
                l_val.append(temp + cur.right.val)
        return False