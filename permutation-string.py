class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Better Solution
        if len(s2) < len(s1):
            return False

        s1_frequencies = [0] * 26
        s2_frequencies = [0] * 26

        for i in range(len(s1)):
            s1_frequencies[ord(s1[i]) - ord("a")] += 1
            s2_frequencies[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1_frequencies[i] == s2_frequencies[i]:
                matches += 1
        if matches == 26:
            return True

        start, end = 0, len(s1)
        while end < len(s2):
            index = ord(s2[end]) - ord("a")
            s2_frequencies[index] += 1
            if s1_frequencies[index] == s2_frequencies[index]:
                matches += 1
            elif s1_frequencies[index] == s2_frequencies[index] - 1:
                matches -= 1

            index = ord(s2[start]) - ord("a")
            s2_frequencies[index] -= 1
            if s1_frequencies[index] == s2_frequencies[index]:
                matches += 1
            elif s1_frequencies[index] == s2_frequencies[index] + 1:
                matches -= 1

            if matches == 26:
                return True

            start += 1
            end += 1

        return False

        # First Solution

        # frequencies = defaultdict(int)
        # for character in s1:
        #     frequencies[character] += 1

        # start, end = 0, 0
        # while end < len(s2):
        #     frequencies[s2[end]] -= 1
        #     while frequencies[s2[end]] < 0 and start < len(s2):
        #         frequencies[s2[start]] += 1
        #         start += 1

        #     if end - start + 1 == len(s1):
        #         return True

        #     end = max(end + 1, start)

        # return False
