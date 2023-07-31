class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maxave = window / k
        # print(window, maxave, nums[:k])
        for i in range(k, len(nums)):

            window += nums[i] - nums[i - k]
            # print(f"nums[i - k]:{nums[i - k]},nums[k]:{nums[i]} ")
            maxave = max(maxave, window / k)
            # print(window, maxave, nums[i - k + 1:i + 1])

        return maxave

