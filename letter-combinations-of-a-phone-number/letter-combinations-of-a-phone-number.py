class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                answer.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in data[digits[i]]:
                    dfs(i+1, path+j)
        
        data = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        if not digits:
            return []
        
        answer = []
        dfs(0, "")
        
        return answer