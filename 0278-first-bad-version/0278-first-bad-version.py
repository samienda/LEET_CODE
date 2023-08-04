# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import sys
# sys.setrecursionlimit(1000000)
class Solution:
    def firstBadVersion(self, n: int) -> int:

        high = n 
        low = 1
        mid = (low + high) // 2
        # def find(n, low, mid, high):
        #     if isBadVersion(mid):
        #         if not isBadVersion(mid - 1):
        #             return mid
        #         else:
        #             high = mid
        #             mid = (low + mid ) // 2

        #     else:
        #         low = mid
        #         mid = (mid + high) // 2

        #     return find(n, low, mid, high)

        # return find(n, low, mid, high)
        while low <= high:
            mid = (high +low) // 2
            if not isBadVersion(mid):
                if isBadVersion(mid + 1):
                    return mid + 1
                low = mid + 1
            else:
                if not isBadVersion(mid - 1):
                    return mid
                high = mid - 1    

        
            
            