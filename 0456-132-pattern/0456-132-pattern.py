class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        comp = float('-inf')


        for i in range(n - 1, -1, -1):
            if nums[i] < comp:
                return True


            while stack and nums[i] > stack[-1]:
                comp = stack.pop()
            
            stack.append(nums[i])

        return False