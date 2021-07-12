class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(x):
            while graph[x]:
                dfs(graph[x].pop(0))
            answer.append(x)
        
        graph = collections.defaultdict(list)   # 유사 딕셔너리
        for a, b in sorted(tickets):
            graph[a].append(b)

        answer = []
        dfs("JFK")

        return answer[::-1]