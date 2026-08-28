class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        dp = [False]*(target+1); dp[0] = True
        for n in nums:
            for cap in range(target, n-1, -1):
                dp[cap] = dp[cap] or dp[cap-n]
        return dp[target]
        