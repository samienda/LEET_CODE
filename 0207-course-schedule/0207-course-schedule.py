class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        color = [0] * numCourses

        # 0 -> white
        # 1 -> black
        # 2 -> gray


        def dfs(node):
            if color[node] == 1:
                return True

            if color[node] == 2:
                return False

            color[node] = 2 # color the node gray when entering

            for neigh in adj[node]:
                if not dfs(neigh):
                    return False

            color[node] = 1 # color the node black when leaving
            return True
            





        for node in range(numCourses):
            if not dfs(node):
                return False

        return True