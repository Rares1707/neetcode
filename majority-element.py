class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority_element = 0, nums[0]
        for num in nums:
            if num == majority_element:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority_element = num
                    count = 1
        return majority_element
