class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # n = len(piles) // 3
        # alice = 0
        # me = 0
        # bob = 0

        # for i in range(n):
        #     ali = max(piles)
        #     piles.remove(ali)
        #     m = max(piles)
        #     piles.remove(m)
        #     me += m

        # return me


        me = 0
        maxi = max(piles)

        result = [0 for i in range(maxi + 1)]
        for i in piles:
            result[i] += 1

        last = []

        for i in range(maxi + 1):
            for j in range(result[i]):
                last.append(i)

        for i in range(len(piles)//3):
            last.pop()
            m = last.pop()
            me += m


        print(last)
        return me



        