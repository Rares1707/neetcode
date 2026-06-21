class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ("(", "[", "{")
        bracket_pairs = {"{": "}", "[": "]", "(": ")"}

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            elif stack and bracket == bracket_pairs[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
