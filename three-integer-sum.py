class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_found = []

        n = len(nums)
        nums.sort()

        for i in range(n):
            if (
                nums[i] > 0
            ):  # all remaining numbers are positive, the sum cannot become 0
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start, end = i + 1, n - 1
            while start < end:
                current_sum = nums[i] + nums[start] + nums[end]
                if current_sum < 0:
                    start += 1
                elif current_sum > 0:
                    end -= 1
                elif current_sum == 0:
                    triplets_found.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

        return triplets_found
