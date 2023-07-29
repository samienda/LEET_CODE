class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # self.lis = [0]
    def __iter__(self):
        return iter(self.nums)


    def sumRange(self, left: int, right: int) -> int:
        s = sum(self.nums[left:right + 1])
        return s



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)