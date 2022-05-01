class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        def dfs(start:str, end:str):
            visited.add(start)
            if start==end:
                return 1
            for n, dist in adj[start].items():
                if n not in visited:
                    res = dfs(n,end)
                    if res:
                        return dist*res
            return 0
        
        adj = defaultdict(dict)
        for i,(src,dst) in enumerate(equations):
            adj[src][dst] = values[i]
            adj[dst][src] = 1/values[i]
            
        ans = []
        for src,dst in queries:
            if src not in adj.keys() or dst not in adj.keys():
                ans.append(-1)
                
            else:
                visited = set()
                val = dfs(src,dst)
                if val:
                    ans.append(val)
                else:
                    ans.append(-1)
        return ans