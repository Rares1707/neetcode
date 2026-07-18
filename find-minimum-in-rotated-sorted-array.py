class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid + 1 <= end and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[0]
