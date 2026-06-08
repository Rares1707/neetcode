class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for j, potential_letter in enumerate(strs[0]):
            for string in strs[1:]:
                if j >= len(string) or potential_letter != string[j]:
                    return strs[0][:j]
        return strs[0]
