class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_appearance = {}
        start_index = 0
        max_length = 0

        for i, character in enumerate(s):
            if (
                character in last_appearance
                and last_appearance[character] >= start_index
            ):
                start_index = last_appearance[character] + 1
            else:
                max_length = max(max_length, i - start_index + 1)
            last_appearance[character] = i

        return max_length
