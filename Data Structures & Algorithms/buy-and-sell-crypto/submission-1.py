class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ret = 0

        m = prices[0]

        for i in range(n):
            m = min(m, prices[i])
            ret = max(ret, prices[i]-m)
        
        return ret
        

        