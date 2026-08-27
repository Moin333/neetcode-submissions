class Solution:
    def f(self, idx, prev_idx, nums, n, dp):
        if(idx == n): return 0
        if(dp[idx][prev_idx + 1] != -1): return dp[idx][prev_idx + 1]
        len = 0 + self.f(idx + 1, prev_idx, nums, n, dp)
        if(prev_idx == -1 or nums[idx] > nums[prev_idx]):
            len = max(len, 1 + self.f(idx + 1, idx, nums, n, dp))

        dp[idx][prev_idx + 1] = len
        return len

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*n for _ in range(n+1)]
        ans = self.f(0, -1, nums, n, dp)
        return ans