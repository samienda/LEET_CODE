class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)


        visted = [False] * n

        provinces = 0

        def dfs(i):
            visted[i] = True

            for j in range(n):
                if not visted[j] and isConnected[i][j]:
                    dfs(j)


        for i in range(n):
            if not visted[i]:
                provinces += 1
                dfs(i)

        return provinces
