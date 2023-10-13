class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = 2 * k + 1
        sums = 0
        result = [-1] * n

        for i in range(n):
            sums += nums[i]

            if  i - window >= 0:
                sums -= nums[i - window]

            if i >= window - 1:
                result[i - k] = sums // window



        return result
        