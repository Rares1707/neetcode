class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for character in string:
                counts[ord(character) - ord("a")] += 1
            groups[tuple(counts)].append(string)
        return list(groups.values())
