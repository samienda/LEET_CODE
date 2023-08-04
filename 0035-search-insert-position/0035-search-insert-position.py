class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        mid = len(nums) // 2
        high = len(nums)
        # nums.sort()
        def search(lis, x, low, mid, high):
            if lis[mid] == x:
                return mid

            if len(lis[low:high]) == 1:
                if lis[mid] > x :
                    return low
                else:
                    return high
            elif lis[mid] > x:
                high = mid 
                mid = (mid + low ) // 2
            else:
                low = mid 
                mid = (high + mid) // 2

            return search(lis, x, low, mid, high)

        return search(nums, target, low, mid, high)


