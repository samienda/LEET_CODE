class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        def traverse(lis, idx):
            if idx >= len(lis) - 1:
                return lis
            
            lis[idx + 1] += lis[idx]

            return traverse(lis, idx + 1)

        return traverse(nums, 0) 