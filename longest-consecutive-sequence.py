class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence_length = 0
        nums = set(nums)

        for number in nums:
            if number - 1 not in nums:
                sequence_length = 1
                while number + 1 in nums:
                    sequence_length += 1
                    number += 1
                max_sequence_length = max(max_sequence_length, sequence_length)

        return max_sequence_length
