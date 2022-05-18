# Took help from a youtube video
# link - https://www.youtube.com/watch?v=5xUdS0hclQ4

G = defaultdict(list)
        for v, w in connections:
            G[v].append(w)
            G[w].append(v)
        self.time = 0
        visited = set()
        visited_time = defaultdict(int)
        parent = defaultdict(lambda:float('inf'))
        res = []
        def dfs(v):
            if v in visited: return visited_time[v]
            visited.add(v)
            visited_time[v] = self.time
            self.time += 1
            highest = float('inf')
            for w in G[v]:
                if w in visited:
                    if w != parent[v]:
                        highest = min(highest,visited_time[w])
                else:
                    parent[w] = v
                    highest_w = dfs(w)
                    if highest_w > visited_time[v]:
                        res.append([v,w])
                    highest = min(highest, highest_w)
            return highest
        dfs(0)
        return res