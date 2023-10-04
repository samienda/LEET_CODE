class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # me = 0
        # maxi = max(piles)

        # result = [0 for i in range(maxi + 1)]
        # for i in piles:
        #     result[i] += 1

        # last = []

        # for i in range(maxi + 1):
        #     for j in range(result[i]):
        #         last.append(i)

        # for i in range(len(piles)//3):
        #     last.pop()
        #     m = last.pop()
        #     me += m

        # return me


        piles.sort()
        result = 0
        left = 0
        right = len(piles) - 2

        while left < right:
            result += piles[right]


            left += 1
            right -= 2

        return result



        