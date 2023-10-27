class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        seen = {0:-1}
        n  = len(nums)


        for i in range(n):
            prefix += nums[i]


            if k != 0:
                prefix %= k


            if prefix in seen:
                if i - seen[prefix] > 1:
                    return True
            else:
                seen[prefix] = i

        return False