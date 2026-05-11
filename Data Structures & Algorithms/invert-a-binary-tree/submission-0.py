# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.inTree(root)

    def inTree(self,root:Optional[TreeNode]):
        if root is None:
            return
        self.inTree(root.left)
        self.inTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root

        