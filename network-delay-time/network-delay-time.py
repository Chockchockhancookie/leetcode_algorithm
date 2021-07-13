class Solution:    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        INF = int(1e9)
    
        def dijkstra(start, graph):
            distance = [INF] * (n+1)
            distance[start] = 0
            queue = []
            heapq.heappush(queue, (0, start))
            while queue:
                dist, now = heapq.heappop(queue)
                if distance[now] < dist:
                    continue
                for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(queue, (cost, i[0]))

            check = True
            total = 0
            for i in range(1, n+1):
                if distance[i] == INF:
                    return False
                else:
                    total = max(total, distance[i])
            return total
        
        graph = [[] for _ in range(n+1)]
        for start, end, dist in times:
            graph[start].append([end, dist])
        
        answer = dijkstra(k, graph)
        
        if answer == False:
            return -1
        else:
            return answer