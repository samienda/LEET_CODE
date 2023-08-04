# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def traverse(root):
            nonlocal count
            if not root:
                return (0,0)


            lcount, lsum = traverse(root.left)
            rcount, rsum = traverse(root.right)

            tsum = root.val + lsum + rsum
            tcount = 1 + lcount + rcount

            if tsum // tcount == root.val:
                count += 1

            return tcount, tsum


        traverse(root)
        return count
                