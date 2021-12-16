class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        G = {}
        for i in range(n):
            G[i] = []
        outdegree = collections.defaultdict(int) 
        for a, b in edges:
            G[a].append(b)
            outdegree[a] += 1
            G[b].append(a)
            outdegree[b] += 1
        outs = []
        for i in range(n):
            if outdegree[i] == 1:
                outs.append(i)
        
        if len(outs) == 0:
            return [0]
        if len(outs) == n:
            return outs
        order = []
        result = []
        while outs:
            temp = []
            for node in outs:
                order.append(node)
                for nbr in G[node]:
                    outdegree[nbr] -= 1
                    if outdegree[nbr] == 1:
                        temp.append(nbr)
            outs = temp
            if temp:
                result = temp
        return result