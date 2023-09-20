# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque([root])

        while queue:
            length = len(queue)
            sumof = 0

            for i in range(length):
                node = queue.popleft()
                sumof += node.val


                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


            result.append(sumof/length)

        return result