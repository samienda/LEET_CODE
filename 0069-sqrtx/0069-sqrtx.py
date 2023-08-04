class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 2 or x == 3:
            return 1
        low = 0
        high = x
        mid = x // 2

        while low < high:
            mid = (high + low) // 2
            if (mid ** 2) > x:
                if ((mid - 1)**2) < x:
                    return mid -1 
                high = mid
            elif mid** 2 < x:
                if (mid + 1) ** 2 > x:
                    return mid
                low = mid
            else:
                return mid


        return mid
