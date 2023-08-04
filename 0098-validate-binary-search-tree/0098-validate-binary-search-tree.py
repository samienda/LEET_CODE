# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = (-2)**33
        maxi = 2**33 - 1 

        def traverse(root , mini, maxi):
            if not root:
                return True

            data = root.val
            if data >= maxi  or data <= mini:
                return False


            left = traverse(root.left, mini, data) 
            right = traverse(root.right, data, maxi) 

            return left and right

        return traverse(root, mini, maxi)
        