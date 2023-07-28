class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def check(n):
            if n < 2:
                return n==1
                
            n /= 4 
            return check(n)

        return check(n)