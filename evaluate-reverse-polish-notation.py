class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second_number = stack.pop()
                first_number = stack.pop()
                if token == "+":
                    result = first_number + second_number
                elif token == "-":
                    result = first_number - second_number
                elif token == "*":
                    result = first_number * second_number
                elif token == "/":
                    result = int(first_number / second_number)
                stack.append(result)
        return stack[0]
