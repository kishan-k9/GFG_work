class Solution:
    def articulationPoints(self, V, edges):

        from collections import defaultdict
        # Create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        disc = [-1] * V # discovery time of nodes
        low = [-1] * V # lowest discovery time reachable
        parent = [-1] * V
        ap = [False] * V # articulation point markers
        time = [0] # single-item list to be mutable in dfs
        def dfs(u):
            children = 0
            disc[u] = low[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if disc[v] == -1: # If v is not visited
                    parent[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    # If u is not root and low[v] >= disc[u], it's an AP
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                    # If u is root and has more than one child
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends