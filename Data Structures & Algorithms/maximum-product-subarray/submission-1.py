class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            if val < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(val, cur_max * val)
            cur_min = min(val, cur_min * val)
            global_max = max(global_max, cur_max)

        return global_max