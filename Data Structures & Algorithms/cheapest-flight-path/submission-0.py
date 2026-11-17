class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp[i][j]  = min cost to fly to dest j when it is the ith stop
        dp = [[float("inf")] * n for _ in range(k+2)]
        dp[0][src] = 0

        res = float("inf")

        for i in range(1, k+2):
            for s, d, price in flights:
                dp[i][d] = min(dp[i][d], dp[i-1][s] + price)
                if d == dst:
                    res = min(res, dp[i][d])

        return -1 if res == float("inf") else res

        