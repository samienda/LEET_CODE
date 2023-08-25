class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        # 1 -> color A
        # -1 -> color B

        def dfs(node, color):
            if colors[node] != 0:
                return colors[node] == color

            colors[node] = color

            for neigh in graph[node]:
                if not dfs(neigh, -color):
                    return False
            return True


            
        
        
        for i in range(len(graph)):
            if colors[i] == 0 and not dfs(i, 1):
                return False

        return True