class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for number in nums:
            if number in my_set:
                return True
            my_set.add(number)
        return False  # handles the empty set too
