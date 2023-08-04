# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root):
            if not root:
                return root
        
            if p.val > root.val and q.val > root.val:
                return traverse(root.right)
            elif p.val < root.val and q.val < root.val:
                return traverse(root.left)
            else:
                return root

        return traverse(root)

