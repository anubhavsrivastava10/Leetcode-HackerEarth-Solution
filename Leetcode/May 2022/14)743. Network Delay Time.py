class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashtable = defaultdict(list)
        
        for item in times:
            hashtable[item[0]].append((item[2],item[1]))
                
        visited = set()
        heap = [(0,k)]
        while heap:
            # print(visited)
            # print(heap)
            time, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited) == n:
                return time
            
            for nodetime, adjnode in hashtable[node]:
                # print(nodetime, adjnode)
                if adjnode not in visited:
                    heapq.heappush(heap, (time+nodetime, adjnode))
        return -1