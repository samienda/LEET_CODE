class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        graph = defaultdict(set)


        for src, dest in roads:
            graph[src].add(dest)     
            graph[dest].add(src)

        # print(graph)    


        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                print("node1", node1)
                print("node2", node2)
                currRank = len(graph[node1]) + len(graph[node2])
                if node2 in graph[node1]:
                    currRank -= 1

                maxRank = max(maxRank, currRank)


        return maxRank
