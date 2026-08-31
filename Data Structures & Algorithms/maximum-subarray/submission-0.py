class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            global_max_sum = max(global_max_sum, cur_sum)
        return global_max_sum