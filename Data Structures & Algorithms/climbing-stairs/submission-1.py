class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n + 1)

        def f(n):
            if n <= 2: return n
            if dp[n]: return dp[n]

            dp[n] = f(n - 1) + f(n - 2)
            return dp[n]
        
        return f(n)