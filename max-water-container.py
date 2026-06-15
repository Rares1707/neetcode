class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        start, end = 0, len(heights) - 1
        while start < end:
            current_volume = (end - start) * min(heights[start], heights[end])
            if current_volume > max_volume:
                max_volume = current_volume

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_volume
