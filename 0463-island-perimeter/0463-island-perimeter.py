class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(grid, i, j):
            # if not (0 < i <= n) or not (0< j <= m) or grid[i][j] == 0:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 1

            if grid[i][j] == 2:
                return 0
            
            grid[i][j] = 2


            return (
                dfs(grid, i + 1, j)+
                dfs(grid, i, j + 1)+
                dfs(grid, i - 1, j)+
                dfs(grid, i, j - 1)
            )





        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return dfs(grid , r, c)


