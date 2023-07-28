class Solution:
    def fib(self, n: int) -> int:
        # fibi = []
        # fibi.append (0)
        # fibi.append(1)
        # for i in range(2,n + 1):
        #     fibi.append( fibi[i - 1] + fibi[i - 2] )

        # return fibi[n]

        def fibo(n):
            if n == 1 or n == 0:
                return n 

            n = fibo(n-2) + fibo(n-1)

            return n

        return fibo(n)
                