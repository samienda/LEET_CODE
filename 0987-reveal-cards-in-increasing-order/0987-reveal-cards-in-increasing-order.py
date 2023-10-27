class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n= len(deck)
        deck.sort()


        # queue = deque(range(n))
        # result = [0] * n

        # for card in deck:
        #     result[queue.popleft()] = card

        #     if queue:
        #         queue.append(queue.popleft())


        # return result


        # # or 

        queue = deque()
        for card in deck[::-1]:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)

        return queue