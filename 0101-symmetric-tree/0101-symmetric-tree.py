# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(lroot, rroot):
            if not rroot or not lroot:
                if rroot or lroot:
                    return False
                return True
            

            if lroot.val != rroot.val:
                return False

            left = traverse(lroot.left, rroot.right)
            right = traverse(lroot.right, rroot.left)
            
            return left and right
            

        return traverse(root.left, root.right)