class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        n = len(parent)
        
        for i in range(n):
            if parent[i] != -1 :
                graph[parent[i]].append(i)
                graph[i].append(parent[i])


        @cache
        def dfs(node, parent):
            count = 1
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if s[neigh] != s[node]:
                    count = max(count, dfs(neigh, node) + 1)

            return count



        
        return max(dfs(i, -1) for i in range(n))
               
