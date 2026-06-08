class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_removed, k = 0, 0
        n = len(nums)
        while k + count_removed < n:
            if nums[k] == val:
                count_removed += 1
                nums[k] = nums[n - count_removed]
            else:
                k += 1
        return k
