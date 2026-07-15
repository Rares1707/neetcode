class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        smallest_valid_k = None

        while start <= end:
            k = (start + end) // 2

            # check validity
            number_of_hours_passed = 0
            for pile in piles:
                if number_of_hours_passed > h:
                    break
                number_of_hours_passed += (pile - 1) // k + 1

            if number_of_hours_passed <= h:
                smallest_valid_k = k
                end = k - 1
            else:
                start = k + 1

        return smallest_valid_k
