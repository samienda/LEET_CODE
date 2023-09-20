class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        n, m = len(grid), len(grid[0])
        time, fresh = 0, 0

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                    continue
                if grid[r][c] == 2:
                    queue.append([r, c])


        

        while queue and fresh > 0:

            print(queue, "fresh", fresh)
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row , col = r + dr, c + dc 
                    if ( not(0 <= row < n) or not(0 <= col < m) or grid[row][col] != 1 ):
                        continue

                    grid[row][col] = 2
                    fresh -= 1
                    queue.append([row, col])    
            time += 1

        
        return time if fresh == 0 else -1