class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # no empty string case, the problem constraints do not include it
        if len(s) != len(t):
            return False

        unicode_offset = ord("a")
        letter_frequency = [0] * 26

        for letter in s:
            letter_frequency[ord(letter) - unicode_offset] += 1

        for letter in t:
            index = ord(letter) - unicode_offset
            if letter_frequency[index] == 0:
                return False
            letter_frequency[index] -= 1

        return True
