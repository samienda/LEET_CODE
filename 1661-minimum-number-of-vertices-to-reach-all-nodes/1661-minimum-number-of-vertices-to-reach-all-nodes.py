class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        lis = [0] * n
        for src, dest in edges:
            lis[dest] += 1

        nlis = []
        idx = 0

        for i in range(n):
            if lis[i] == 0 :
                nlis.append(i)

        
        return nlis
