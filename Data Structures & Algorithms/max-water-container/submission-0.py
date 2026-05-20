class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i = 0
        j = len(heights) - 1

        while i < j:

            height = min(heights[i], heights[j])
            width = j - i

            curr_area = height * width

            max_area = max(curr_area, max_area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area