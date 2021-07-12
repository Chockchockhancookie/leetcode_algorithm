class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(x, a, data):
            if x == target:
                answer.append(data)
                return
            elif x > target:
                return
            
            for i in range(a, len(candidates)):
                dfs(x + candidates[i], i, data + [candidates[i]])
        
        
        answer = []
        dfs(0, 0, [])
        return answer