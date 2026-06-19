class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency, max_frequency = defaultdict(int), 0
        max_length = 0

        start = 0
        for end in range(len(s)):
            frequency[s[end]] += 1
            max_frequency = max(max_frequency, frequency[s[end]])

            if end - start + 1 > max_frequency + k:  # invalid window
                frequency[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
