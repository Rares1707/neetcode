class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # simple solution with O(n) extra space complexity
        # repeated = [False] * len(nums)
        # for num in nums:
        #     if repeated[num]:
        #         return num
        #     repeated[num] = True

        # O(1) extra space complexity, still O(n) time complexity
        # I don't like this solution because you must memorize the algorithm.
        # The proof of the algorithm is certainly not trivial.
        # The explanation from the video is not the complete proof because it assumes the fast
        # pointer completes exactly one cycle before the slow one enters the cycle. This is false,
        # think of the case where the cycle is formed only by the last two nodes and there are
        # many nodes before the beginning of the cycle. Here is the actual proof:
        # https://www.geeksforgeeks.org/dsa/how-does-floyds-slow-and-fast-pointers-approach-work/.
        # Again, it is not trivial by any means.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        second_slow = 0
        while True:
            second_slow = nums[second_slow]
            slow = nums[slow]
            if slow == second_slow:
                return slow
