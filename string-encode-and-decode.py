class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num_characters = int(s[i:j])

            string_start = j + 1
            string_end = j + num_characters
            decoded_strings.append(s[string_start : string_end + 1])

            i = string_end + 1

        return decoded_strings
