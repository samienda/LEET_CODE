class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = sum(nums)
        n = len(nums)
        # value = sums - target

        if sums < target:
            return 0


        length = n
        curr = 0
        left = 0

        for right in range(n):
            curr += nums[right]
            

            while curr >= target:
                length = min(length, right - left + 1)    
                curr -= nums[left]
                left += 1
            
            


        return length
