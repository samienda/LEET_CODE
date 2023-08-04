# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        k = root
        def traverse(root):
            nonlocal k
            if not root:
                k = root
                return root

            if root.val > val:
                traverse(root.left)
            elif root.val < val:
                traverse(root.right)
            elif root.val == val:
                k = root
                return k
                
        traverse(root)


        return k