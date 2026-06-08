class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in indices:
                return [indices[diff], index]
            indices[number] = index
