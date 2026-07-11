class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            temperature = temperatures[i]

            while stack and temperature > stack[-1][0]:
                _, original_index = stack.pop()
                result[original_index] = i - original_index
            stack.append((temperature, i))

        return result
