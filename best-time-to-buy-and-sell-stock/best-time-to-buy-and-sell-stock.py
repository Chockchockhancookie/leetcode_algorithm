class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        price = int(1e9)
        
        for a in prices:
            price = min(price, a)
            answer = max(answer, a - price)
        
        return answer