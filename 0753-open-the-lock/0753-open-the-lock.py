class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visted = set(deadends)
        queue = deque()
        queue.append(['0000', 0])
        if '0000' in visted:
            return -1


        while queue:
            state, level = queue.popleft()

            for i in range(4):
                for move in (-1, 1):

                    if state == target:
                        return level

                    next_state = state[:i] + str((int(state[i]) + move) % 10) + state[i+1:]
                    if next_state not in visted:
                        visted.add(next_state)
                        queue.append((next_state, level + 1))

        return -1