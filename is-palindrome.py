class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if not self.is_alpha_numeric(s[start]):
                start += 1
                continue
            if not self.is_alpha_numeric(s[end]):
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True

    def is_alpha_numeric(self, character):
        return (
            "a" <= character <= "z"
            or "A" <= character <= "Z"
            or "0" <= character <= "9"
        )
